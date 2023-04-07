from django.shortcuts import render
from rest_framework.views import APIView
from customUser.forms import UserProfileForm
from customUser.models import User
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class updateUser(APIView):
    """
    Seperate vocals and music from songs
    - Assign celery task to Seperate Audio
    - Return celery task_id in response
    """
    def post(self, request):
        username = request.data['username']
        data = User.objects.get(username=username)
        update_user = UserProfileForm(request.POST,request.FILES, instance=data)
        update_user.profilePic = request.data['profilePic']
        update_user.userInfo = request.data['userInfo']
        # # data.update(profilePic=request.data['profilePic'])
        # # data.update(userInfo=request.data['userInfo'])
        update_user.save()
        print(data, request.data,request.FILES)
        return Response('Saved', status=status.HTTP_200_OK)