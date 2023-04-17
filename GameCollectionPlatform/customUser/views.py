from django.shortcuts import render
from rest_framework.views import APIView
from customUser.forms import UserProfileForm
from customUser.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny 
from rest_framework.decorators import permission_classes 
# Create your views here.
class updateUser(APIView):
    """
    Seperate vocals and music from songs
    - Assign celery task to Seperate Audio
    - Return celery task_id in response
    """
    print("inside")
    def put(self, request):
        username = request.data['username']
        user = get_object_or_404(User, username=username)
        data=request.data
        for field in data:
            if hasattr(user, field):
                setattr(user, field, data[field])
        user.save()
        serializer = UserDetailsSerializer(user,context={'request':request})
        return Response(serializer.data)
    @permission_classes([AllowAny])
    def get(self, request, *args, **kwargs):
        user= User.objects.all()
        serializer = UserDetailsSerializer(user, many=True,context={'request':request})
        return Response(serializer.data)
    def delete(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        if username is not None:
            user = get_object_or_404(User, username=username)
            user.delete()
            return Response({'message': f'User {username} has been deleted.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Username parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        print("INSIDE ")
        user_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
                username = request.data['username']
                email = request.data.get('password',None)
                password = request.data.get('password',None)
                first_name = request.data.get('firstName',None)
                last_name = request.data.get('lastName',None)
                user_type = request.data.get('userType',None)
                profile_pic = request.data['profilePic']
                user_info = request.data['userInfo']
                date_of_birth = request.data.get('dateOfBirth',None)
                location = request.data.get('location', None)  # This field is optional
                # Create a new user using the UserManager
                print(request)
                new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    firstName=first_name,
                    lastName=last_name,
                    userType=user_type,
                    profilePic=profile_pic,
                    userInfo=user_info,
                    dateOfBirth=date_of_birth,
                    location=location,
                )
                user_serializer = UserDetailsSerializer(new_user,context={'request':request})
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        else:
            # If the form is not valid, return an error response with a bad request status code (400)
            return Response(user_form.errors, status=status.HTTP_400_BAD_REQUEST)
    
