from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from . import views
from .views import UserViewSet, CustomLoginView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.registration_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('api/', include(router.urls)),
    path('auth/', include('social_django.urls', namespace='social')),
]
