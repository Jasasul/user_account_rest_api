import factory
from pytest_factoryboy import register
import pytest

from rest_framework.test import APIClient

from django.core import serializers
from django.contrib.auth.models import User

from . import NUM_OF_TEST_USERS, REGISTER_URL

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

# Create your tests here.
@pytest.fixture()
def test_client():
    client = APIClient()

    yield client


@pytest.fixture()
def users(db):
    users = []
    for i in range(NUM_OF_TEST_USERS):
        user = new_user_json()
        User.objects.create(
            username=user['username'],
            email=user['email'],
            password=user['password']
        )
        users.append(user)
    
    yield users


@pytest.fixture()
def user():
    yield new_user_json()