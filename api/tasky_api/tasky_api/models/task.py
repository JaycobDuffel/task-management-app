from django.db import models
from .project import Project
from .stage import Stage

class Task(models.Model):
    identifier = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.identifier