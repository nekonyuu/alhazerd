from django import forms

class UploadPictureForm(forms.Form):
    sentImage = forms.FileField()
