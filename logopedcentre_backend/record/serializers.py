from rest_framework import serializers
from .models import Direction, DirectionPoints, Specialist


class DirectionPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionPoints
        fields = (
            "id",
            "description",    
        )

# class SpecialistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Specialist
#         fields = (
#             "id",
#             "name",
#             "sname",
#             "tname",
#             "slug",
#             "get_absolute_url",
#             "get_image",
#             "get_thumbnail",
#         )


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = (
            "id",
            "name",
            "sname",
            "tname",
            "slug", 
        )

class DirectionSpecialistSerializer(serializers.ModelSerializer):
    directionpoints = DirectionPointsSerializer(many = True)
    specialists = SpecialistSerializer(many = True)
    class Meta:
        model = Direction
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "directionpoints",
            "specialists",
        )

class DirectionSerializer(serializers.ModelSerializer):
    directionpoints = DirectionPointsSerializer(many = True)
    specialists = SpecialistSerializer(many = True)
    class Meta:
        model = Direction
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "directionpoints",
            "specialists",
        )

