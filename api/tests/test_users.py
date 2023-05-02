import pytest

from django.contrib.auth.models import User

from . import USERS_URL

@pytest.mark.django_db()
def test_users(test_client, users):
    # view should display all existing users
    # in this case the number of test users created
    response = test_client.get(USERS_URL)
    assert(response.status_code == 200)
    assert(len(response.data) == User.objects.count())