from django.shortcuts import render
from rest_framework.views import APIView
from customUser.forms import UserProfileForm
from customUser.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserDetailsSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
class updateUser(APIView):
    """
    Seperate vocals and music from songs
    - Assign celery task to Seperate Audio
    - Return celery task_id in response
    """
    def put(self, request):
        username = request.data['username']
        data = User.objects.get(username=username)
        update_user = UserProfileForm(request.POST,request.FILES, instance=data)
        update_user.profilePic = request.data['profilePic']
        update_user.userInfo = request.data['userInfo']
        # # data.update(profilePic=request.data['profilePic'])
        # # data.update(userInfo=request.data['userInfo'])
        print(update_user.profilePic)
        update_user.save()
        print(data, request.data,request.FILES)
        return Response('Saved', status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        username = request.query_params.get('username', None)
        if username is not None:
            user = get_object_or_404(User, username=username)
            user_serializer = UserDetailsSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Username parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        if username is not None:
            user = get_object_or_404(User, username=username)
            user.delete()
            return Response({'message': f'User {username} has been deleted.'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Username parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        user_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
                username = request.data['username']
                email = request.data['email']
                password = request.data['password']
                first_name = request.data['firstName']
                last_name = request.data['lastName']
                user_type = request.data['userType']
                profile_pic = request.data['profilePic']
                user_info = request.data['userInfo']
                date_of_birth = request.data['dateOfBirth']
                location = request.data.get('location', None)  # This field is optional
                collection=request.data.get('collection')
                # Create a new user using the UserManager
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
                    collection=collection
                )
                user_serializer = UserDetailsSerializer(new_user)
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        else:
            # If the form is not valid, return an error response with a bad request status code (400)
            return Response(user_form.errors, status=status.HTTP_400_BAD_REQUEST)
    
