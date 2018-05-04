from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.html import format_html


class ContentRow(models.Model):
    PAGE_CHOICES = (
        ('ABOUT', 'About'),
        ('CONTACT', 'Contact'),
    )

    description = models.CharField(max_length=200)
    content = models.TextField()
    page = models.CharField(max_length=200, choices=PAGE_CHOICES, default='ABOUT')
    priority = models.IntegerField()

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-priority']


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
