from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GamePublisher,PublisherManager
from .forms import GamePublisherForm
from .serializers import GamePublisherSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes 


@api_view(['GET'])
@permission_classes([AllowAny])
def publisher_list(request):
    publisher = GamePublisher.objects.all()
    serializer = GamePublisherSerializer(publisher, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def publisher_create(request):
        data=request.data
        files = request.FILES
        if isinstance(files.get('profilePicture', None), InMemoryUploadedFile):
            data['profilePicture'] = files['profilePicture']
        serializer = GamePublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def publisher_detail(request, publisher_code):
    publisher = get_object_or_404(GamePublisher, publisherCode=publisher_code)
    if request.method == 'GET':
        serializer = GamePublisherSerializer(publisher)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = request.data
        for field in data:
            if field=='pubPassword':
                manager=PublisherManager()
                check=manager.is_password_complex(data[field])
                if not check:
                     raise ValidationError("Password does not meet complexity requirements")
            if hasattr(publisher, field):
                setattr(publisher, field, data[field])
        publisher.save()
        serializer = GamePublisherSerializer(publisher)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=204)



