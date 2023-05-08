import pytest

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from . import USERS_URL

@pytest.mark.django_db()
def test_users(test_client, users, admin_token):
    # view should display all existing users
    # in this case the number of test users created
    test_client.credentials(HTTP_AUTHORIZATION=f'{admin_token}')
    response = test_client.get(USERS_URL)
    assert(response.status_code == 200)
    assert(len(response.data) == User.objects.count())