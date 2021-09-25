from exception.custom_exception import (
    PermissionError,
    AuthException,
    UsernameAlreadyExists,
    PasswordTooShort,
    InvalidUsername,
    InvalidPassword,
    NotLoggedInError,
    NotPermittedError,
)
from user import User


class Authenticator:
    def __init__(self):
        "build authenticator to manage user login and logout"
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False