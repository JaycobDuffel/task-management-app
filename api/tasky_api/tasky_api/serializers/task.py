from rest_framework import serializers

from tasky_api.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'identifier', 'description', 'project', 'stage')