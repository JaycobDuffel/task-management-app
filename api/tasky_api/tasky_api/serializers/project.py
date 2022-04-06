from rest_framework import serializers

from tasky_api.models import Project
from tasky_api.serializers.task import TaskSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    task = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('pk', 'title', 'description', 'task')