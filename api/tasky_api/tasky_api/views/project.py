from rest_framework import viewsets

from tasky_api.serializers import ProjectSerializer
from tasky_api.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer