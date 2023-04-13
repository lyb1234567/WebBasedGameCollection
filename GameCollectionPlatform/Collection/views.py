from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import GameCollection
from .serializers import GameCollectionSerializer
from .forms import GameCollectionForm
from rest_framework import status
from django.core.exceptions import ValidationError


@api_view(['GET'])
def game_collection_list(request):
    game_collections = GameCollection.objects.all()
    serializer = GameCollectionSerializer(game_collections, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def game_collection_create(request):
    if request.method == 'POST':
        user_id = request.data.get('user')
        game_id = request.data.get('game')
        # Check if the user already has a game with the same game code
        existing_game = GameCollection.objects.filter(user_id=user_id, game=game_id)
        if existing_game.exists():
            return JsonResponse({'error': 'This user already has a game with the same game code in their collection.'},
                                status=status.HTTP_400_BAD_REQUEST)

        serializer = GameCollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def game_collection_detail(request, collection_code):
    game_collection = get_object_or_404(GameCollection, collectionCode=collection_code)
    if request.method == 'GET':
        serializer = GameCollectionSerializer(game_collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        for field in data:
            if field == 'game':
                game_collection.game.set(data[field])
            else:
                if hasattr(game_collection, field):
                    setattr(game_collection, field, data[field])
        game_collection.save()
        serializer = GameCollectionSerializer(game_collection)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        game_collection.delete()
        return Response(status=204)

@api_view(['PUT'])
def game_collection_add(request, collection_code):
    game_collection = get_object_or_404(GameCollection, collectionCode=collection_code)
    if request.method == 'PUT':
        data = request.data
        for field in data:
            if field == 'game':
                game_collection.game.add(data[field])
            else:
                raise ValueError("You can only add game in this page")
        game_collection.save()
        serializer = GameCollectionSerializer(game_collection)
        return Response(serializer.data)

@api_view(['PUT'])
def game_collection_delete(request, collection_code):
    game_collection = get_object_or_404(GameCollection, collectionCode=collection_code)
    if request.method == 'PUT':
        data = request.data
        for field in data:
            if field == 'game':
                game_collection.game.remove(data[field])
            else:
                raise ValueError("You can only add game in this page")
        game_collection.save()
        serializer = GameCollectionSerializer(game_collection)
        return Response(serializer.data)


