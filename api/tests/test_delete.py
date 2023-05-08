import pytest

from . import USER_URL


@pytest.mark.django_db
def test_delete(test_client, user_token):
    test_client.credentials(HTTP_AUTHORIZATION=f'{user_token["token"]}')
    response = test_client.delete(
        USER_URL
    )

    assert(response.status_code == 204)