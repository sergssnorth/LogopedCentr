from rest_framework import serializers
from .models import Direction, DirectionPoints, Specialist, UserInformation, UserChildrenInformation
from rest_framework.authtoken.models import Token

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

class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = (
            "name",
            "sname",
            "tname",
            "phone",
            "passport"
        )

class UserChildrenInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChildrenInformation
        fields = (
            "id",
            "name",
            "sname",
            "tname",
            "oms",
            "snils",
            "svidetelstvo"
        )

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = (
            "key",
            "user_id",
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

