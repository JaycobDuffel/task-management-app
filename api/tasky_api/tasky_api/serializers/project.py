from rest_framework import serializers

from tasky_api.models import Project
from tasky_api.serializers.task import TaskSerializer

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('pk', 'title', 'description')