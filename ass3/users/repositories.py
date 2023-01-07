from typing import Optional, List

from users.models import User
from bankAccount import BankAccount


class UserRepositories():

    users: List[User] = []

    def create_user(self, username: str, password: str) -> None:
        user = User(username=username, bank_account=BankAccount(username))
        user.set_password(password=password)

        self.users.append(user)

    def get_user(self, username: str, password: str) -> Optional[User]:

        for u in self.users:
            if username == u.username and u.check_password(password=password):
                return u

        return 'User not found'












