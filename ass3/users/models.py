import hashlib
from dataclasses import dataclass, field
from bankAccount import BankAccount


@dataclass
class User:
    username: str
    _password: str = field(init=False)
    bank_account: BankAccount = field(repr=False)

    def set_password(self, password: str) -> None:
        self._password = self.hash_password(password)

    def check_password(self, password: str) -> bool:
        return self._password == self.hash_password(password)

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()



