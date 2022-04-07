from django.contrib import admin
from .models import Task, Stage, Project

admin.site.register(Task)
admin.site.register(Stage)
admin.site.register(Project)