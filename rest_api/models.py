import json
from django.core.serializers import serialize
from django.db import models
from django.conf import settings

class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = list(self.values('id','user','content','image'))
        return json.dumps(qs)

class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)
class UpdateModel(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)


    objects     = UpdateManager()   

    def __str__(self):
        return self.content

    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
        data = {
            'id':self.id,
            'user_id': self.user.id,
            'content': self.content,
            'image': image
        }
        json_data = json.dumps(data)
        return json_data
    





