from rest_framework import serializers
from apps.direction.models import Direction


class DirectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'
        