from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.core.validators import EmailValidator

from django.contrib.auth.models import User


MAX_USERNAME_LENGTH = 50
MAX_EMAIL_LENGTH = 256
MAX_PASSWORD_LENGTH = 25


def validate_length(value, length):
    if len(value) > length:
        raise serializers.ValidationError(
            f'The maximum length is {length} chars'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
    )

    class Meta:
        model = User
        fields = ['username', 'password']



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all()),
            lambda x: validate_length(x, MAX_USERNAME_LENGTH) 
        ]
    )
    email = serializers.EmailField(
        required=False,
        allow_blank=True,
    )
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        validators=[
            lambda x: validate_length(x, MAX_PASSWORD_LENGTH)
        ]
    )

    class Meta(LoginSerializer.Meta):
        fields = ('username', 'email', 'password')


    def create(self, validated_data):
        email = validated_data.get('email')
        user = User.objects.create(
            username=validated_data['username'],
            email=email if email else ''
        )
        user.set_password(validated_data['password'])
        user.save()

        return user