from django.db import models


class Image(models.Model):
    file = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.file.name

    def url(self):
        return self.file.url
