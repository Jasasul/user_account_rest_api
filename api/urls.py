from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='users-list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token)
]