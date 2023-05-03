import factory
from pytest_factoryboy import register
import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.core import serializers
from django.contrib.auth.models import User

from . import NUM_OF_TEST_USERS, REGISTER_URL, LOGIN_URL

class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
    password = factory.Sequence(lambda n: 'pass%d' % n)

register(UserFactory)

def get_user_json(user):
    return {
        'username':  user.username,
        'email': user.email,
        'password': user.password
    }

def new_user_json():
    user = UserFactory()

    return {
        'username':  user.username,
        'email': user.email,
        'password': user.password
    }


def register_assert(test_client, data, expected_code):
    response = test_client.post(
        REGISTER_URL,
        data
    )

    assert(response.status_code == expected_code)


def get_token(test_client, user):
    login_json = {}

    if user.get('username'):
        login_json['username'] = user['username']

    if user.get('password'):
        login_json['password'] = user['password']

    response = test_client.post(
        LOGIN_URL,
        login_json
    )

    return response.data.get('token')

# Create your tests here.
@pytest.fixture()
def test_client():
    client = APIClient()

    yield client


@pytest.fixture()
def users():
    users = []
    for i in range(NUM_OF_TEST_USERS):
        user = new_user_json()
        user_obj = User.objects.create(
            username=user['username'],
            email=user['email'],
        )
        user_obj.set_password(user['password'])
        user_obj.save()
        token = Token.objects.create(user=user_obj)
        token.save()
        users.append(user)
    
    yield users


@pytest.fixture()
def user():
    yield new_user_json()