from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from userCRUD.models import User
from userCRUD.serializers import UserSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def user_create(request):
    user_data = JSONParser().parse(request)
    users_serializer = UserSerializer(data=user_data)
    if users_serializer.is_valid():
        users_serializer.save()
        return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED) 
    return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_read(request):
    user = User.objects.all()
    users_serializer = UserSerializer(user, many=True)
    return JsonResponse(users_serializer.data, safe=False)
 

@api_view(['DELETE'])
def user_delete(request, username):
    user = User.objects.get(username=username)
    user.delete() 
    return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def user_update(request, username):
    user = User.objects.get(username=username)
    user_data = JSONParser().parse(request) 
    user_serializer = UserSerializer(user, data=user_data) 
    if user_serializer.is_valid(): 
        user_serializer.save() 
        return JsonResponse(user_serializer.data, status=status.HTTP_200_OK) 
    return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 