from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GameModel
from .forms import GameForm
from .serializers import GameSerializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes 

@api_view(['GET'])
@permission_classes([AllowAny])
def game_list(request):
    game = GameModel.objects.all()
    serializer = GameSerializers(game, many=True,context={'request':request})
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def game_create(request):
    if request.method == 'POST':
        data=request.data
        files = request.FILES
        if isinstance(files.get(' gameicon', None), InMemoryUploadedFile):
            data[' gameicon'] = files[' gameicon']
        serializer = GameSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def game_detail(request, game_code):
    game = get_object_or_404(GameModel, gameCode=game_code)
    if request.method == 'GET':
        serializer = GameSerializers(game, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        for field in data:
            if hasattr(game, field):
                setattr(game, field, data[field])
        game.save()
        serializer = GameSerializers(game)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def game_add(request, game_code):
    game = get_object_or_404(GameModel, gameCode=game_code)
    if request.method == 'PUT':
        data = request.data
        for field in data:
            if field == 'collection':
                game.collection.add(data[field])
            else:
                raise ValueError("You can only add collection in this page")
        game.save()
        serializer = GameSerializers(game)
        return Response(serializer.data)

@api_view(['PUT'])
def game_delete(request, game_code):
    game = get_object_or_404(GameModel, gameCode=game_code)
    if request.method == 'PUT':
        data = request.data
        for field in data:
            if field == 'collection':
                game.collection.remove(data[field])
            else:
                raise ValueError("You can only delete collection in this page")
        game.save()
        serializer = GameSerializers(game)
        return Response(serializer.data)
