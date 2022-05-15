from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def login(request):
    return Response('This is login')


@api_view(['GET'])
def logout(request):
    return Response('This is logout')


@api_view(['GET'])
def signup(request):
    return Response('This is signin')


@api_view(['GET'])
def signout(request):
    return Response('This is signout')
