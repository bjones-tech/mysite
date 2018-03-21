from django.contrib import admin

from .models import Tag, Solution


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


class SolutionAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'featured']
    filter_horizontal = ['tags']


admin.site.register(Tag, TagAdmin)
admin.site.register(Solution, SolutionAdmin)
