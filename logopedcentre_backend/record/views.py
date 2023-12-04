from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Direction, DirectionPoints, Specialist
from django.http import Http404
from .serializers import DirectionSerializer, SpecialistSerializer


class LatestDirectionsList(APIView):
    def get(self, request, format=None):
        directions = Direction.objects.all()
        serializer = DirectionSerializer(directions, many = True)
        return Response(serializer.data)

class LatestSpecialistsList(APIView):
    def get(self, request, format=None):
        specialist = Specialist.objects.all()
        serializer = SpecialistSerializer(specialist, many = True)
        return Response(serializer.data)



class DirectionSpecialistsList(APIView):
    def get(self, request, direction_id, format=None):
        specialist = Specialist.objects.filter(direction_id = direction_id)
        serializer = SpecialistSerializer(specialist, many = True)
        return Response(serializer.data)
    
# class DirectionSpecialistsList(APIView):
#     def get_object(self, request, direction_slug):
#         try:
#             return Direction.objects.get(id = direction_slug)
#         except Product.DoesNotExist:
#             raise Http404
        
#     def get(self, request, category_slug, format = None):
#         category = self.get_object(category_slug)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
    

class DirectionPointsDetail(APIView):
    def get_object(self, direction_slug):
        try:
            return DirectionPoints.objects.get(direction = direction_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, direction_slug, format = None):
        category = self.get_object(direction_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)