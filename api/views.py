from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiResponse, extend_schema_view

from django.contrib.auth.models import User

from .serializers import UserSerializer, RegisterSerializer, UpdateSerializer

ERROR_MESSAGES = {
    400: OpenApiResponse(
        description='Invalid input',
    ),
    401: OpenApiResponse(
        description='Missing/Bad authentication header',
    ),
    403: OpenApiResponse(
        description='You are not an admin'
    ),
}

@extend_schema(
    description='Returns a list of users',
    responses={
        200: UserSerializer(many=True),
        400: ERROR_MESSAGES[400],
        401: ERROR_MESSAGES[401],
        403: ERROR_MESSAGES[403]
    },
)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]



@extend_schema(
    auth=None,
    description='Registers a new user',
    responses={
        200: RegisterSerializer(many=True),
        400: ERROR_MESSAGES[400],
    }
)
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

   

@extend_schema_view(
    get=extend_schema(
        description="Returns the current user's details",
        responses={
            200: UserSerializer(many=True),
            400: ERROR_MESSAGES[400],
            401: ERROR_MESSAGES[401],
        }
    ),
    put=extend_schema(
        exclude=['PUT'],
    ),
    patch=extend_schema(
        description="Updates the user's details",
        responses={
            200: UserSerializer(many=True),
            400: ERROR_MESSAGES[400],
            401: ERROR_MESSAGES[401],
        }
    ),
    delete=extend_schema(
        description="Delete's the user's account",
        responses={
            204: OpenApiResponse(
                description='Account was deleted'
            ),
            400: ERROR_MESSAGES[400],
            401: ERROR_MESSAGES[401],
            403: OpenApiResponse(
                description='The last admin account cannot be deleted'
            )
        }
    ),
)
class UserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateSerializer
        return UserSerializer
    
    def update(self, request, *args, **kwargs):
        # PUT is redundant since PATCH is used to update details
        if request.method == 'PUT':
            return Response(
                {'detail': 'Method "PUT" not allowed'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
        return super().update(request, *args, **kwargs)