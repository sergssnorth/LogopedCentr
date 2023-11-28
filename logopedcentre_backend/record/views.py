from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Direction
from django.http import Http404
from .serializers import DirectionSerializer


class LatestDirectionsList(APIView):
    def get(self, request, format=None):
        directions = Direction.objects.all()
        serializer = DirectionSerializer(directions, many = True)
        return Response(serializer.data)