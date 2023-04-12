from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GamePublisher
from .forms import GamePublisherForm
from .serializers import GamePublisherSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile
@api_view(['GET', 'POST'])
def publisher_list(request):
    if request.method == 'GET':
        publishers = GamePublisher.objects.all()
        serializer = GamePublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
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
def publisher_detail(request, pk):
    publisher = get_object_or_404(GamePublisher, pk=pk)

    if request.method == 'GET':
        serializer = GamePublisherSerializer(publisher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        for field in data:
            if hasattr(publisher, field):
                setattr(publisher, field, data[field])
        publisher.save()
        serializer = GamePublisherSerializer(publisher)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

