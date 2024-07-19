from django.shortcuts import render
from . import models as md
from . import serializers as se
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['POST'])
def postar(request): #criando um novo post 
    post=se.postS(data=request.data)
    if md.post.objects.filter(**request.data).exists():
        raise se.ValidationError('This data already exists')
 
    if post.is_valid():
        post.save()
        return Response(post.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
def cadastrar_se():
    pass
def logar():
    pass

def mostrar_post():
    pass

def apaga_user():
    pass
