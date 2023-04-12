from django.urls import path
from . import views

app_name = 'Game'
urlpatterns = [
    # ... other urlpatterns ...
    path('games/create/', views.GameCreateView.as_view(), name='game_create'),
]