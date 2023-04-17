from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer,ReviewSerializerCreate
from rest_framework import status
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes 
# Create your views here.

@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()
    # for r in review:
    #     print(r.game)
    serializer = ReviewSerializer(review, many=True,context={'request':request})
    # print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def review_create(request):
    if request.method == 'POST':
        publisher=request.data.get('publisher')
        user=request.data.get('user')
        if (publisher !=None and user !=None):
             return JsonResponse({'error': 'A review uploader can not both user and publisher'},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = ReviewSerializerCreate(data=request.data)
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
        data = request.data
        for field in data:
            if hasattr(review, field):
                setattr(review, field, data[field])
        review.save()
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)

