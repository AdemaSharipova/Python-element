from dataclasses import dataclass
from typing import Optional

from users.models import User
from users.interfaces import UserServicesInterface


@dataclass
class UserHandlers:
    services: UserServicesInterface

    def create_user(self, username: str, password: str) -> None:
        username = username.strip().lower()
        password = password.strip()

        self.services.create_user(username=username, password=password)

    def get_user(self, username: str, password: str) -> Optional[User]:
        username = username.strip().lower()
        password = password.strip()

        return self.services.get_user(username=username, password=password)


