from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import decorators, get_user_model 
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

class SignUpAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def signup(request):
    
#     pass

# @decorators.login_required
# def signout(request):
#     pass

# def login(request):
#     pass

# @decorators.login_required
# def logout(request):
#     pass

# @decorators.login_required
# def profile(request):
#     pass
