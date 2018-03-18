from ckeditor.fields import RichTextField
from django.db import models


class Solution(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = RichTextField()
    release_date = models.DateField()
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
