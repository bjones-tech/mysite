from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'url']


admin.site.register(Image, ImageAdmin)
