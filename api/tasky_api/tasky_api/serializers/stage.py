from rest_framework import serializers

from tasky_api.models import Stage

class StageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stage
        fields = ('pk', 'title', 'order')