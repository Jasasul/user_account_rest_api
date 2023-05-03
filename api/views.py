from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import authenticate
from rest_framework import generics

from django.contrib.auth.models import User

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

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


class LoginViewSet(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(username=username, password=password)

            if not user:
                return Response(
                    {'error': 'Invalid credentials'},
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            token, _ = Token.objects.get_or_create(user=user)

            return Response(
                {'token': token.key},
                status=status.HTTP_200_OK
            )
            
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )