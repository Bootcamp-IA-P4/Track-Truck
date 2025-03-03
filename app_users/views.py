from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['GET'])
def getAllUsers(request):
    books = User.objects.all() 
    serializer = UserSerializer(books, many=True) 
    return Response(serializer.data)
