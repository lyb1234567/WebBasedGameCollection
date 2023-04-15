"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path ,re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from customUser import views as userViews
from GamePublisher.views import publisher_create,publisher_list,publisher_detail
from Game.views import game_detail,game_list,game_create,game_delete,game_add
from Collection.views import game_collection_create,game_collection_detail,game_collection_list,game_collection_add,game_collection_delete
from Review.views import review_create,review_list,review_detail
from Community.views import community_create,community_detail,community_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',TemplateView.as_view(template_name = 'index.html'), name= 'index'),
    path('api/', include('loginRegister.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/user/update/',userViews.updateUser.as_view()),
    path('api/v1/publishers/', publisher_list, name='publisher_list'),
    path('api/v1/publishers/create/', publisher_create, name='publisher_list'),
    path('api/v1/publishers/<int:publisher_code>/', publisher_detail, name='publisher_detail'),
    path('api/v1/game/', game_list, name='game_list'),
    path('api/v1/game/create/', game_create, name='game_create'),
    path('api/v1/game/<int:game_code>/', game_detail, name='game_detail'),
    path('api/v1/game/<int:collection_code>/add/', game_add, name='game_add'),
    path('api/v1/game/<int:collection_code>/delete/', game_delete, name='game_delete'),
    path('api/v1/game-collections/', game_collection_list, name='game_collection_list'),
    path('api/v1/game-collections/create/', game_collection_create, name='game_collection_create'),
    path('api/v1/game-collections/<int:collection_code>/add/', game_collection_add, name='game_collection_add'),
    path('api/v1/game-collections/<int:collection_code>/delete/', game_collection_delete, name='game_collection_delete'),
    path('api/v1/game-collections/<int:collection_code>/', game_collection_detail, name='game_collection_detail'),
    path('api/v1/review/', review_list, name='review_list'),
    path('api/v1/review/create/', review_create, name='review_create'),
    path('api/v1/review/<int:review_code>/', review_detail, name='review_detail'),
    path('api/v1/community/', community_list, name='community_list'),
    path('api/v1/community/create/', community_create, name='community_create'),
    path('api/v1/community/<int:community_code>/', community_detail, name='community_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
