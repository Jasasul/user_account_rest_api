import json
import factory
from pytest_factoryboy import register
import pytest

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from django.core import serializers
from django.contrib.auth.models import User

from . import NUM_OF_TEST_USERS, REGISTER_URL, LOGIN_URL, USER_URL

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

def new_user_json(user=None):
    if not user:
        user = UserFactory()

    return {
        'username':  user.username,
        'email': user.email,
        'password': user.password
    }


def register_assert(test_client, data, expected_code):
    response = test_client.post(
        REGISTER_URL,
        json.dumps(data),
        content_type='application/json'
    )

    assert(response.status_code == expected_code)


def update_assert(test_client, user, new_data, token, expected_code):
    test_client.credentials(HTTP_AUTHORIZATION=f'{token}')
    response =test_client.put(
        USER_URL,
        json.dumps(new_data),
        content_type='application/json'
    )

    if expected_code != 200:
        assert(response.status_code == expected_code)
        return

    user = User.objects.get(id=user['id'])
    
    assert(response.status_code == expected_code)

    user = User.objects.get(id=user.id)

    if new_data.get('username'):
        assert(user.username == new_data['username'])
    
    if new_data.get('email'):
        assert(user.email == new_data['email'])

    if new_data.get('password'):
        assert(user.check_password(new_data['password']))


def register_user(user_json=None):
    if not user_json:
        user_json = new_user_json()
    user = User(username=user_json['username'], email=user_json['email'])
    user.set_password(user_json['password'])
    user.save()

    return user


def make_token(user):
    token = Token.objects.create(user=user)
    token.save()

    return f'Token {token.key}'


def get_token(test_client, user):
    login_json = {}

    if user.get('username'):
        login_json['username'] = user['username']

    if user.get('password'):
        login_json['password'] = user['password']

    response = test_client.post(
        LOGIN_URL,
        login_json,
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
        user = register_user()
        make_token(user)

        users.append(user)
    
    yield users


@pytest.fixture()
def user():
    yield new_user_json()


@pytest.fixture()
def user_token():
    user_json = new_user_json()
    user = register_user(user_json)
    user_json['id'] = user.id
    token = make_token(user)

    yield {'user': user_json, 'token': token}