from django.contrib import admin

from .models import Project, Tag, ProjectStat, ProjectLink, Experience


# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(ProjectStat)
admin.site.register(ProjectLink)

admin.site.register(Experience)