from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def review_list(request):
    game_collections = Review.objects.all()
    serializer = ReviewSerializer(game_collections, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def review_create(request):
    if request.method == 'POST':
        publisher=request.data.get('publisher')
        user=request.data.get('user')
        if (int(publisher)>0 and int(user)>0):
             return JsonResponse({'error': 'A review uploader can either be user or publisher'},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_code):
    review = get_object_or_404(Review, reviewCode=review_code)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)

