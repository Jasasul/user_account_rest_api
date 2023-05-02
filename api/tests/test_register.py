from django.contrib.auth.models import User

from . import REGISTER_URL
from .conftest import new_user_json, register_assert

from api.serializers import MAX_USERNAME_LENGTH, MAX_EMAIL_LENGTH, MAX_PASSWORD_LENGTH

def test_register(test_client, users, user):
    register_assert(test_client, user, 201)


def test_register_duplicate_username(test_client, users): 
    register_assert(test_client, users[0], 400)


def test_register_no_username(test_client, users, user): 
    del user['username']

    register_assert(test_client, user, 400)


def test_regiter_blank_username(test_client, users, user):
    user['username'] = ''

    register_assert(test_client, user, 400)


def test_regiter_long_username(test_client, users, user):
    user['username'] = (MAX_USERNAME_LENGTH + 1)*'a'

    register_assert(test_client, user, 400)


def test_register_no_email(test_client, users, user):
    del user['email']

    register_assert(test_client, user, 201)


def test_register_blank_email(test_client, users, user):
    user['email'] = ''

    register_assert(test_client, user, 201)


def test_register_long_email(test_client, users, user):
    local = 200*'a'
    domain = 200*'b'
    email = f'{local}@{domain}.test'
    user['email'] = email

    register_assert(test_client, user, 400)


def test_register_email_format(test_client, users, user):
    formats = [
        'no_ad',
        'no_dot@'
        'no_dot@test'
    ]

    for email in formats:
        user['email'] = email
        register_assert(test_client, user, 400)
    

def test_register_no_password(test_client, users, user):
    del user['password']

    register_assert(test_client, user, 400)


def test_register_blank_password(test_client, users, user):
    user['password'] = ''

    register_assert(test_client, user, 400)


def test_register_long_password(test_client, users, user):
    user['password'] = (MAX_PASSWORD_LENGTH + 1)*'a'

    register_assert(test_client, user, 400)