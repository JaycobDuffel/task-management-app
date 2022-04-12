from django.db import models
from .project import Project

class Stage(models.Model):
    title = models.CharField(max_length=30)
    order = models.IntegerField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title