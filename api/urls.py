from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view(), name='users-list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginViewSet.as_view(), name='login')
]