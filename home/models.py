from django.db import models
from django.utils.html import format_html


class Image(models.Model):
    file = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.file.name

    def url(self):
        return self.file.url

    def thumbnail(self):
        return format_html('<img src="{}" height="150px">', self.file.url)
