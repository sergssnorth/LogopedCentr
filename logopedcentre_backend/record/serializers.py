from rest_framework import serializers
from .models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )