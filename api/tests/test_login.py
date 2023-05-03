import pytest

from .conftest import get_token
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_login(test_client, users):
    assert(get_token(test_client, users[0]))


def test_login_no_username(test_client, user):
    del user['username']
    assert(not get_token(test_client, user))


def test_login_blank_username(test_client, user):
    user['username'] = ''
    assert(not get_token(test_client, user))


def test_login_no_password(test_client, user):
    del user['password']
    assert(not get_token(test_client, user))


def test_login_blank_password(test_client, user):
    user['password'] = ''
    assert(not get_token(test_client, user))