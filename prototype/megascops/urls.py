from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import CustomLoginView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.registration_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('auth/', include('social_django.urls', namespace='social')),
]
