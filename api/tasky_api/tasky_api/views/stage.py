from rest_framework import viewsets

from tasky_api.serializers import StageSerializer
from tasky_api.models import Stage


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all().order_by('id')
    serializer_class = StageSerializer