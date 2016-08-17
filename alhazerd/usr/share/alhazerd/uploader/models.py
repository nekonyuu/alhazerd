from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

import string, random, os

class Pictures(models.Model):
    def generateFileName(self):
        length = random.randint(25,25)  
        letters = string.ascii_letters + string.digits
        return ''.join([random.choice(letters) for _ in range(length)])  
    
    def upload_path_fullPict(self, filename):
        fileName = self.generateFileName()
        return 'fullsize/%s.%s' % (fileName, filename.split('.')[-1])
    
    def upload_path_thumbnail(self, filename):
        fileName = self.generateFileName()
        return 'thumbnails/%s.jpg' % fileName
    
    user = models.ForeignKey(User)
    fullPict = models.ImageField(upload_to=upload_path_fullPict)
    thumbnailPath = models.ImageField(upload_to=upload_path_thumbnail)
    uploadDate = models.DateTimeField('upload date')

# Deleting file when delete signal sent
@receiver(models.signals.post_delete, sender=Pictures)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.fullPict:
        if os.path.isfile(instance.fullPict.path):
            os.remove(instance.fullPict.path)
    if instance.thumbnailPath:
        if os.path.isfile(instance.thumbnailPath.path):
            os.remove(instance.thumbnailPath.path)
