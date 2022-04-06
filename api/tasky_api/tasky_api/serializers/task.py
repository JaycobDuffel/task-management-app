from rest_framework import serializers

from tasky_api.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('pk', 'identifier', 'description')