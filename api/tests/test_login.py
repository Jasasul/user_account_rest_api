import pytest


from .conftest import get_token


@pytest.mark.django_db
def test_login(test_client, user_token):
    assert(get_token(test_client, user_token['user']))


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