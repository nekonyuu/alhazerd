from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

import re

import GlueMethods
import UploaderForms

def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', \
        { "username" : request.user.username, \
          "isUserLoggedIn" : request.user.is_authenticated() }, \
          context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

def logon(request):
    if "username" in request.POST and "password" in request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                # Disabled account
                return render_to_response('index.html', context_instance=RequestContext(request))
        else:
            # Incorrect
            return render_to_response('index.html', context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def logoff(request):
    logout(request)
    return HttpResponseRedirect('/')

def register(request):
    d = { "isUserLoggedIn" : request.user.is_authenticated() }
    if request.method == 'POST':
        username = request.POST["username"]
        mail = request.POST["mail"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if re.match("^.[0-9a-zA-Z@_\+\.\-]+", username) == None:
            d["usernameIncorrect"] = True
            d["usernameErrorMessage"] = "Username can only contains 0-9, A-Z, a-z, @, _ and -"
        
        if password1 <> password2:
            d["passwordMismatch"] = True
            d["passwordErrorMessage"] = "Passwords differs"
        
        if not (len(mail) > 7 and \
            (re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", mail) != None)):
            d["mailIncorrect"] = True
            d["mailErrorMessage"] = "Mail incorrect" 
        
        if len(d) > 1:
            return render_to_response('register.html', d, context_instance=RequestContext(request))
        else:
            user = User.objects.create_user(username, mail, password1)
            authUser = authenticate(username=username, password=password1)
            login(request, authUser)
            return HttpResponseRedirect('/')
    else:
        return render_to_response('register.html', d, context_instance=RequestContext(request))
        

def list_user_gallery(request, username):
    gallery = GlueMethods.get_pictures_by_username(username)
    if not request.user.is_authenticated():
        #return render_to_response('show_gallery.html', \
        #    { "isUserLoggedIn" : request.user.is_authenticated(), \
        #      "galleryList" : gallery },
        #    context_instance=RequestContext(request))
        return HttpResponseRedirect('/')
    else:
        return render_to_response('show_gallery.html', \
            { "username" : request.user.username, \
              "isUserLoggedIn" : request.user.is_authenticated(), \
              "galleryList" : gallery },
            context_instance=RequestContext(request))

def show_user_picture(request, picture_id):
    thumbnail, fullImage = GlueMethods.get_picture(picture_id)
    if not request.user.is_authenticated():
        return render_to_response('show_picture.html', \
        { "isUserLoggedIn" : request.user.is_authenticated(), \
          "imagePath" : fullImage, \
          "thumbnailPath" : thumbnail },
        context_instance=RequestContext(request))
    else:    
        return render_to_response('show_picture.html', \
        { "username" : request.user.username, \
          "isUserLoggedIn" : request.user.is_authenticated(), \
          "imagePath" : fullImage, \
          "thumbnailPath" : thumbnail },
        context_instance=RequestContext(request))

def delete_user_picture(request, picture_id):
    GlueMethods.delete_picture(request.user, picture_id)    
    return HttpResponseRedirect('/user/%s/' % request.user)

def upload_picture(request):
    if request.user.is_authenticated() and request.method == 'POST':
        form = UploaderForms.UploadPictureForm(request.POST, request.FILES)
        if form.is_valid():
            fileID = GlueMethods.handle_uploaded_picture(request.user, \
                request.FILES['sentImage'])
            return HttpResponseRedirect('/picture/%s/' % fileID)
        else:
            return HttpResponseRedirect('/') 
    else:
        return HttpResponseRedirect('/') 

