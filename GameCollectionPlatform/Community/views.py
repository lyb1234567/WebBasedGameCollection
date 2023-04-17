from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Community
from .serializers import CommunitySerializer
from rest_framework import status
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes 

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def community_list(request):
    game_collections = Community.objects.all()
    serializer = CommunitySerializer(game_collections, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def community_create(request):
    if request.method == 'POST':
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def community_detail(request, community_code):
    community = get_object_or_404(Community, communityCode=community_code)
    if request.method == 'GET':
        serializer = CommunitySerializer(community)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        print('data:',data)
        for field in data:
            if hasattr(community, field):
                setattr(community, field, data[field])
        community.save()
        serializer = CommunitySerializer(community)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        community.delete()
        return Response(status=204)
    
@api_view(['PUT'])
def review_add(request, community_code):
    community = get_object_or_404(Community, communityCode=community_code)
    if request.method == 'PUT':
        data = request.data
        for field in data:
            if field == 'review':
                community.review.add(data[field])
            else:
                raise ValueError("You can only add review in this page")
        community.save()
        serializer = CommunitySerializer(community)
        return Response(serializer.data)
