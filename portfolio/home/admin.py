from django.contrib import admin
from .models import Projects

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'published_date')

admin.site.register(Projects, ProjectAdmin)
