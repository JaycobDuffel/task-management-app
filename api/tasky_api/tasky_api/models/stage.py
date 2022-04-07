from django.db import models
from .project import Project

class Stage(models.Model):
    title = models.CharField(max_length=30, unique=True)
    order = models.IntegerField(blank=True)
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.title