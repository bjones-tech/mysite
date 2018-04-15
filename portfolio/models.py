from ckeditor.fields import RichTextField
from django.db import models


class Tag(models.Model):
    CATEGORY_CHOICES = (
        ('LANGUAGE', 'Language'),
        ('FRAMEWORK', 'Framework'),
        ('INTEGRATION', 'Integration'),
    )

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='LANGUAGE')

    def __str__(self):
        return self.name

    def count(self):
        return self.solution_set.count()

    class Meta:
        ordering = ['category', 'name']


class Solution(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = RichTextField()
    release_date = models.DateField()
    featured = models.BooleanField(default=False)
    description_only = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
