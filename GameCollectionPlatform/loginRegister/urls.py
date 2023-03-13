from django.urls import path
from rest_framework import routers
from .views import LoginViewSet

router = routers.DefaultRouter()
router.register('Login', LoginViewSet)

urlpatterns = router.urls