from rest_framework import viewsets

from tasky_api.serializers import TaskSerializer
from tasky_api.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer