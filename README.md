# User account management REST API in Python

## About
This is my take on a RESTful API. I used Python's framework Django.\
Users can craete and manage their accounts by makin API requests.\
On some routes an user must authenticate using a token provied.

This project helped me to get a grasp of what a RESTful API really is. It helped me
to understand different HTTP methods and when should I use which.
And last but not least I improved my test writing skills by writing some test cases
for the API in Pytest.

Example of this site is hosted [here](jasasul.pythonanywhere.com).

The documentation is built in
[swagger](https://jasasul.pythonanywhere.com/docs/).

## Installation
### Docker
You can run the docker image by running the command `docker compose up`

### Raw
The project is built in Python 3.10.
If you don't want to run the image, you can install the project with the following steps.
1. Clone the repository to your machine.
2. In the repository run the command `pip install -r requirements.txt`.
3. **Optional** The migrations are already included but if you want to start with a clean database.
delete the file `db.sqlite3` and run `./manage.py migrate`.
4. Run the server with `./manage.py runserver`.
5. The server will be running at http://localhost:8000.

## Routes
You can set the base URL in the `rest_api/settings.py` file.\
Users are authenticated using tokens.\
Register to create an account.\
Login to that account to receive your token.\
Use the token in **Authorization** headers like so `Authorization: Token <token>`.\

- **docs/** documentation built in *swagger ui*
- **schema/** swagger ui schema
- **register/**
    - **POST** provide `username`, `email (optional)` and `password` to create an user account
- **login/**
    - **POST** provide `username` and `password` to receive your authentication token
- **user/me** user account is detected from the token
    - **GET** fetch your account's details
    - **PATCH** update your account's details. All fields are optional
    - **DELETE** delete your account
- **users/** must be an admin to user this route
    - **GET** fetch all users' details
