from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GameModel
from .forms import GameForm
from .serializers import GameSerializers
from django.core.files.uploadedfile import InMemoryUploadedFile
@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        gamemodel = GameModel.objects.all()
        serializer = GameSerializers(gamemodel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data=request.data
        files = request.FILES
        if isinstance(files.get('gameicon', None), InMemoryUploadedFile):
            data['gameicon'] = files['gameicon']
        serializer = GameSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def game_detail(request, pk):
    game = get_object_or_404(GameModel, pk=pk)

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
