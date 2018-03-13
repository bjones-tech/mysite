from django.contrib import admin

from .models import Solution


class SolutionAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'featured']


admin.site.register(Solution, SolutionAdmin)
