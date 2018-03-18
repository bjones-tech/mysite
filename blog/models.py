from ckeditor.fields import RichTextField
from django.db import models


class Post(models.Model):
    CONTENT_TYPE_CHOICES = (
        ('DOCUMENT', 'Document'),
        ('VIDEO', 'Video'),
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = RichTextField()
    content_type = models.CharField(max_length=200, choices=CONTENT_TYPE_CHOICES, default='DOCUMENT')
    publish_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
