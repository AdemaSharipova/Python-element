from dataclasses import dataclass, field
from enum import Enum


class Account(Enum):
    USD = 'USD'
    RUB = 'RUB'
    KZT = 'KZT'
    EUR = 'EUR'


@dataclass
class BankAccount:

    name: str = ''
    surname: str = ''
    account: Account = Account.KZT
    _sum: float = field(default=0, init=False)

    def set_sum(self, sum: float) -> None:
        self._sum = sum

    def get_sum(self) -> float:
        return self._sum

    def add_to_bank_account(self, sum_to_add) -> float:
        self._sum += sum_to_add
        return self._sum

    def subtract_from_bank_account(self, sum_to_subtract) -> float:
        self.set_sum(self.get_sum() - sum_to_subtract)
        return self.get_sum()

    def money_conversion(self, sum_to_convert, from_currency: Account, to_currency:Account) -> float:

        if from_currency == Account.USD and to_currency == Account.KZT:
            return sum_to_convert * 463
        elif from_currency == Account.KZT and to_currency == Account.USD:
            return sum_to_convert / 463
        elif from_currency == Account.EUR and to_currency == Account.KZT:
            return sum_to_convert * 490
        elif from_currency == Account.KZT and to_currency == Account.EUR:
            return sum_to_convert / 490
        elif from_currency == Account.RUB and to_currency == Account.KZT:
            return sum_to_convert / 7
        elif from_currency == Account.KZT and to_currency == Account.RUB:
            return sum_to_convert * 7

    def __repr__(self):
        return f'BankAccount: surname={self.surname} name={self.name} account={self.account}'

    def __del__(self):
        print('object distracted')
