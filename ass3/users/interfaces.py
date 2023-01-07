from typing import Protocol, Optional, List

from users.models import User


class UserRepositoriesInterface(Protocol):

    users: List[User] = []

    def create_user(self, username: str, password: str) -> None:
        raise NotImplemented

    def get_user(self, username: str, password: str) -> Optional[User]:
        raise NotImplemented



class UserServicesInterface(Protocol):

    repositories: UserRepositoriesInterface

    def create_user(self, username: str, password: str) -> None:
        raise NotImplemented

    def get_user(self, username: str, password: str) -> Optional[User]:
        raise NotImplemented

