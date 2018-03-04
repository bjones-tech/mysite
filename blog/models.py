from django.db import models


class Post(models.Model):
    CONTENT_TYPE_CHOICES = (
        ('DOCUMENT', 'Document'),
        ('VIDEO', 'Video'),
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.TextField()
    content_type = models.CharField(max_length=200, choices=CONTENT_TYPE_CHOICES, default='DOCUMENT')
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
