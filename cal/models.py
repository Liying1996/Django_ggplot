from django.db import models

# Create your models here.


class Upload(models.Model):
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to='upload/')

    def __unicode__(self):
        return self.title
