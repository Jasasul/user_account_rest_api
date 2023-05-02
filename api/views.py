from rest_framework import viewsets, status
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.conf import settings

from .serializers import UserSerializer, RegisterSerializer
from .mixins import CreateOnlyMixin, ListOnlyMixin


class UserViewSet(ListOnlyMixin, viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer



class RegisterViewSet(CreateOnlyMixin, viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        print(settings.SETTINGS_MODULE)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )