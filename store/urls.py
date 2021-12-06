from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) 
from appStore import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()), 
    path('user/', views.UserCreateView.as_view()), 
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('admin/', admin.site.urls),
]
