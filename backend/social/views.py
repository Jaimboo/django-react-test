from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from social.models import Post
from social.serializers import *

# Create your views here.

@api_view(['GET', 'POST'])
def posts_list(request):

    if request.method == 'GET':
        data = Post.objects.all()

        serializer = PostSerializer(data, context={'request':request}, many=True)

        return Response(serializer.data)
    
    elif request.method == 'POST':
     
        serializer = PostSerializer(data = request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT','DELETE'])
def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PostSerializer(post, context={'request':request},)
        return Response(serializer.data)
    
    if request.method == 'PUT':

        serializer = PostSerializer(post, data=request.data, context={'request':request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    