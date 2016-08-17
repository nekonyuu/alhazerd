from uploader.models import Pictures
from django.contrib.auth.models import User
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist

import Image
import tempfile
import os
import magic
import datetime
import string

def handle_uploaded_picture(fromUsername, pict):
    # Checking filetype
    m = magic.open(magic.MAGIC_MIME)
    m.load()
    if m.buffer(pict.read(1024)).find("image") == -1:
        return; # Abort
    pict.seek(0)
    # Making thumbnail
    thumbnailSize = 128, 128
    thumbFileFD, thumbFilePath = tempfile.mkstemp()
    tmpFileThumb = os.fdopen(thumbFileFD, "rwb+")
    try:
        thumbnail = Image.open(pict)
        thumbnail.thumbnail(thumbnailSize, Image.ANTIALIAS)
        thumbnail.save(tmpFileThumb, "JPEG")
    except IOError:
        raise
    
    tmpFileThumb.close()
    tmpFileThumb = open(thumbFilePath, "rb+")
    pict.seek(0)
    
    # Inserting in DB
    user = User.objects.get(username = fromUsername)
    p = user.pictures_set.create(fullPict = pict, thumbnailPath = File(tmpFileThumb), uploadDate=datetime.datetime.now())
    
    # Cleaning
    tmpFileThumb.close()
    os.remove(thumbFilePath)
    
    return p.id

def get_picture(pict_id):
    pict = Pictures.objects.get(id = pict_id)
    return (pict.thumbnailPath, pict.fullPict)

def get_pictures_by_username(fromUsername):
    user = User.objects.get(username = fromUsername)
    return user.pictures_set.all()

def delete_picture(fromUsername, pictId):
    user = User.objects.get(username = fromUsername)
    try:
        pict = user.pictures_set.get(pk=pictId)
        pict.delete()
    except ObjectDoesNotExist:
	pass

