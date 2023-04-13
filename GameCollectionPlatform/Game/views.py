from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GameModel
from .forms import GameForm
from .serializers import GameSerializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
@api_view(['GET'])
def game_list(request):
    game = GameModel.objects.all()
    serializer = GameSerializers(game, many=True)
    return Response(serializer.data)

@api_view(['POST'])
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
def game_detail(request, game_code):
    game = get_object_or_404(GameModel, gameCode=game_code)
    if request.method == 'GET':
        serializer = GameSerializers(game)
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
