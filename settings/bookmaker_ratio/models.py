from django.db import models
import os
import uuid

class Bookmaker(models.Model):

    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("static/images", filename)

    name = models.CharField('Name', max_length=255, default=None)
    bonus = models.TextField('Bonus', default=None, blank=True, null=True)
    url = models.CharField('URL',max_length=255, default=None)
    description = models.TextField('Description', default=None, blank=True, null=True)
    image = models.ImageField('Image', upload_to=get_file_path, blank=True, null=True)
    ratio = models.IntegerField('Rating',default=0) #'Star', 'One Two Three Four Five'
