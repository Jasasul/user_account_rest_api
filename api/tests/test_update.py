import pytest

from api.serializers import MAX_USERNAME_LENGTH, MAX_PASSWORD_LENGTH
from .conftest import new_user_json, update_assert

@pytest.mark.django_db
def test_update_all(test_client, user_token):
    new_data = new_user_json()
    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_username(test_client, user_token):
    new_data = new_user_json()
    del new_data['email']
    del new_data['password']

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_duplicate_username(test_client, user_token):
    new_data = {'username': user_token['user']['username']}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_blank_username(test_client, user_token):
    new_data = {'username': ''}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        400
    )


@pytest.mark.django_db
def test_update_long_username(test_client, user_token):
    new_data = {'username': (MAX_USERNAME_LENGTH + 1)*'a'}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        400
    )


@pytest.mark.django_db
def test_update_email(test_client, user_token):
    new_data = new_user_json()
    del new_data['username']
    del new_data['password']

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_duplicate_email(test_client, user_token):
    new_data = {'email': user_token['user']['email']}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_blank_email(test_client, user_token):
    new_data = {'email': ''}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_long_email(test_client, user_token):
    local = 200*'a'
    domain = 200*'b'
    email = f'{local}{domain}.com'
    new_data = {'username': email}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        400
    )


@pytest.mark.django_db
def test_update_email_format(test_client, user_token):
    formats = [
        'no_ad',
        'no_dot@'
        'no_dot@test'
    ]

    for email in formats:
        new_data = {'email': email}

        update_assert(
            test_client,
            user_token['user'],
            new_data,
            user_token['token'],
            400
        )

@pytest.mark.django_db
def test_update_password(test_client, user_token):
    new_data = new_user_json()
    del new_data['username']
    del new_data['email']

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_duplicate_password(test_client, user_token):
    new_data = {'password': user_token['user']['password']}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        200
    )


@pytest.mark.django_db
def test_update_blank_password(test_client, user_token):
    new_data = {'password': ''}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        400
    )


@pytest.mark.django_db
def test_update_long_username(test_client, user_token):
    new_data = {'password': (MAX_PASSWORD_LENGTH + 1)*'a'}

    update_assert(
        test_client,
        user_token['user'],
        new_data,
        user_token['token'],
        400
    )