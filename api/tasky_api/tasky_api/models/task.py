from django.db import models

class Task(models.Model):
    identifier = models.CharField(max_length=20, unique=True)

    stages = (
        ('todo', 'To Do'),
        ('in progress', 'In Progress'),
        ('done', 'Done'),
    )
    stage = models.CharField(max_length=20, choices=stages, default='todo')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.identifier