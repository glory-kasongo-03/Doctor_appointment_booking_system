from typing import List
from .notification import Notification

class UserAccount:
    def __init__(self, user_id: str, username: str, password: str, role: str):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._role = role
        self.notifications: List[Notification] = []

    def login(self):
        print(f"{self._username} logged in.")

    def logout(self):
        print(f"{self._username} logged out.")

    def change_password(self, new_password: str):
        self._password = new_password
        print(f"Password changed for user {self._username}")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
