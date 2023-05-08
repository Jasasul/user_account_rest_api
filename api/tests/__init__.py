from rest_api.settings import BASE_URL

USERS_URL = f'/{BASE_URL}users/'
REGISTER_URL = f'/{BASE_URL}register/'
LOGIN_URL = f'/{BASE_URL}login/'
USER_URL = f'{USERS_URL}me/'

NUM_OF_TEST_USERS = 10