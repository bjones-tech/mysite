from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.html import format_html


class Image(models.Model):
    file = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.file.name

    def url(self):
        return self.file.url

    def thumbnail(self):
        return format_html('<img src="{}" height="150px">', self.file.url)

    def delete_file(self):
        self.file.delete()


@receiver(pre_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    instance.delete_file()
