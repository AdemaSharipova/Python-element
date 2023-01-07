import sys

from users.handlers import UserHandlers
from users.repositories import UserRepositories
from users.services import UserServices
from bankAccount import BankAccount, Account



def init():
    user_repositories = UserRepositories()
    user_services = UserServices(repositories=user_repositories)
    user_handlers = UserHandlers(services=user_services)

    while True:
        command = input('Выберите ваше действие: \n'
                        '1. Создание пользователя \n'
                        '2. Выбрать пользователя \n'
                        '0. Выйти \n')

        if command == '1':
            username, password = input('Введите имя пользователя и пароль: ').split()
            user_handlers.create_user(username=username, password=password)

        elif command == '2':
            username, password = input('Введите имя пользователя и пароль: ').split()
            user = user_handlers.get_user(username=username, password=password)
            print(user)
            while True:
                command2 = input('Выберите дальнейшее действие: \n'
                                 '1. Внести деньги '
                                 '2. Снять деньги '
                                 '3. Конвертация валюты '
                                 '0. Назад \n')

                if command2 == '1':
                    sum_to_add = int(input('Введите сумму: '))
                    print(user.bank_account.add_to_bank_account(sum_to_add))


                elif command2 == '2':
                    sum = int(input('Введите сумму: '))
                    print(user.bank_account.subtract_from_bank_account(sum))

                elif command2 == '3':
                    sum = int(input('Введите сумму: '))
                    from_currency = Account(input('Первая валюта: '))
                    to_currency = Account(input('Вторая валюта: '))
                    print(user.bank_account.money_conversion(sum, from_currency, to_currency))

                elif command2 == '0':
                    break

        elif command == '0':
            sys.exit(0)

init()