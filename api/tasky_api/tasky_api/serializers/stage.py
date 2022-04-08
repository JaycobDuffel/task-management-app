from rest_framework import serializers

from tasky_api.models import Stage

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('pk', 'title', 'order', 'projects')