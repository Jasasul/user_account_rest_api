from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'register', views.RegisterView, basename='register')
router.register(r'login', views.LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
]