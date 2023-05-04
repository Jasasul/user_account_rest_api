from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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



class RegisterSerializer(serializers.ModelSerializer):
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

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegisterSerializer, self).create(validated_data)
    

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(RegisterSerializer, self).update(instance, validated_data)


class UpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
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
        required=False,
        write_only=True,
        style={'input_type': 'password'},
        validators=[
            lambda x: validate_length(x, MAX_PASSWORD_LENGTH)
        ]
    )

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
    

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UpdateSerializer, self).create(validated_data)
    

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        print('username' in validated_data)
        return super(UpdateSerializer, self).update(instance, validated_data)

