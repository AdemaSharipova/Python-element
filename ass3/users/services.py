from dataclasses import dataclass
from typing import Optional

from users.models import User
from users.interfaces import UserRepositoriesInterface


@dataclass
class UserServices():
    repositories: UserRepositoriesInterface

    def create_user(self, username: str, password: str) -> None:
        self.repositories.create_user(username=username, password=password)

    def get_user(self, username: str, password: str) -> Optional[User]:
        return self.repositories.get_user(username=username, password=password)
