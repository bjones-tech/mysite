from django.contrib import admin

from .models import ContentRow, Image


class ContentRowAdmin(admin.ModelAdmin):
    list_display = ['description', 'page', 'priority']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'url']


admin.site.register(ContentRow, ContentRowAdmin)
admin.site.register(Image, ImageAdmin)
