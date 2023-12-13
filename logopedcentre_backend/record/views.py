from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Direction, DirectionPoints, Specialist, UserInformation, UserChildrenInformation, SpecialistSchedule, Record, RecordStatus
from django.http import Http404
from .serializers import DirectionSerializer, SpecialistSerializer, UserInformationSerializer, UserTokenSerializer, UserChildrenInformationSerializer, SpecialistScheduleSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

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
    def get(self, request, direction_slug, format=None):
        specialist = Specialist.objects.filter(direction__slug = direction_slug)
        serializer = SpecialistSerializer(specialist, many = True)
        return Response(serializer.data)
    

class LatestSpecialistShedule(APIView):
    def get(self, request, specialist_id, format=None):
        specialist = SpecialistSchedule.objects.filter(specialist__id = specialist_id).order_by("date")
        serializer = SpecialistScheduleSerializer(specialist, many = True)
        return Response(serializer.data)


class UserIdDetail(APIView):
    def get(self, request, token, format=None):
        user_information = Token.objects.filter(key = token)
        serializer = UserTokenSerializer(user_information, many = True)
        return Response(serializer.data)

class AccountInfoDetail(APIView):
    def get(self, request, user_id, format=None):
        user_information = UserInformation.objects.filter(user_id = user_id)
        serializer = UserInformationSerializer(user_information, many = True)
        return Response(serializer.data)


class AccountChildrensInfoDetail(APIView):
    def get(self, request, user_id, format=None):
        user_children_information = UserChildrenInformation.objects.filter(user_id = user_id)
        serializer = UserChildrenInformationSerializer(user_children_information, many = True)
        return Response(serializer.data)
    

class DeleteAccountDetail(APIView):
    def get(self, request, user_id, format=None):
        user_information = UserInformation.objects.filter(user_id = user_id).delete()
        return Response() 
    
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
    


@api_view(['POST'])
def addInfoAccount(request):
    query = request.data.get('query', '')
    print(query)
    print(request.data)
    if query:
        user = User.objects.get(id = query['user_id']) 
        user_information = UserInformation(user = user, name = query['name'], sname = query['sname'], tname = query['tname'], phone = query['phone'], passport = query['passport'])
        user_information.save()
        return Response()
    else:
        return Response({"products": []})
    

@api_view(['POST'])
def editInfoAccount(request):
    query = request.data.get('query', '')
    print(query)
    print(request.data)
    if query:
        user = User.objects.get(id = query['user_id']) 
        old_user_information = UserInformation.objects.get(user_id = query['user_id'])
        old_user_information.user = user
        old_user_information.name = query['name']
        old_user_information.sname = query['sname']
        old_user_information.tname = query['tname']
        old_user_information.phone = query['phone']

        old_user_information.save()
        return Response()
    else:
        return Response({"products": []})
    

@api_view(['POST'])
def addChildren(request):
    query = request.data.get('query', '')
    print(query)
    print(request.data)
    if query:
        user = User.objects.get(id = query['user_id']) 
        user_сhildren_information = UserChildrenInformation(user = user, name = query['name'], sname = query['sname'], tname = query['tname'], birthdate = query['birthdate'] )
        user_сhildren_information.save()
        return Response()
    else:
        return Response({"products": []})

@api_view(['POST'])
def addRecord(request):
    query = request.data.get('query', '')
    print(query)
    print(request.data)
    if query:
        print("Зашел в функцию")
        user = User.objects.get(id = query['user_id']) 
        children = UserChildrenInformation.objects.get(id = query['children_id']) 
        direction = Direction.objects.get(slug = query['direction_slug']) 
        specialist = Specialist.objects.get(id = query['specialist_id']) 
        record_date = SpecialistSchedule.objects.get(id = query['datetime']) 
        record_status = RecordStatus.objects.get(slug = query['record_slug']) 

        record = Record(user = user, children = children, direction = direction, specialist = specialist, record_date = record_date, status = record_status, comment = query['comment'] )
        record.save()
        return Response()
    else:
        return Response({"products": []})
    
    


    

@api_view(['POST'])
def deleteChildren(request):
    query = request.data.get('query', '')
    print(query)
    print(request.data)
    if query:
        user = User.objects.get(id = query['user_id']) 
        user_сhildren_information = UserChildrenInformation.objects.filter(id=query['children_id'])[0]
        user_сhildren_information.delete()
        return Response()
    else:
        return Response({"products": []})
    
    