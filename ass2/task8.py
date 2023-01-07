class BankAccount():
    accountSumKZT: float = 0
    accountSumUSD: float = 0

    def __int__(self, accountSumKZT=0, accountSumUSD=0):
        self.accountSumKZT = accountSumKZT
        self.accountSumUSD = accountSumUSD

    def addToBankAccount(self, sum, currency="KZT"):
        if currency == "KZT":
            self.accountSumKZT += sum
        elif currency == "USD":
            self.accountSumUSD += sum

    def displayAccountSum(self, currency="KZT"):
        if currency == "KZT":
            return f'{self.accountSumKZT} {currency}'
        elif currency == "USD":
            return f'{self.accountSumUSD} {currency}'


    def substractFromBankAccount(self, sum, currency = "KZT"):
        if currency == "KZT":
            if self.accountSumKZT >= sum:
                self.accountSumKZT -= sum
            else:
                print(f'You don\'t have {sum}')
        elif currency == "USD":
            if self.accountSumUSD >= sum:
                self.accountSumUSD -= sum
            else:
                print(f'You don\'t have {sum}')

    def moneyConversion(self, sum, firstCurrency, secondCurrency):
        if firstCurrency == "USD" and secondCurrency == "KZT":
            if sum <= self.accountSumUSD:
                self.accountSumUSD -= sum
                sum *= 470
                self.accountSumKZT += sum
            else:
                print(f'you don\'t have {sum} {firstCurrency} to convert')
        elif firstCurrency == "KZT" and secondCurrency == "USD":
            if sum <= self.accountSumKZT:
                self.accountSumKZT -= sum
                sum /= 470
                self.accountSumUSD += sum
            else:
                print(f'you don\'t have {sum} {firstCurrency} to convert')
        return f'{sum} {secondCurrency}'


def main():
    Adema_Sharipova = BankAccount()
    Adema_Sharipova.addToBankAccount(500)
    print(Adema_Sharipova.displayAccountSum())
    Adema_Sharipova.substractFromBankAccount(200)
    print(Adema_Sharipova.displayAccountSum())
    print(Adema_Sharipova.moneyConversion(300, "KZT", "USD"))
    print(Adema_Sharipova.displayAccountSum("USD"))
    print(Adema_Sharipova.displayAccountSum())
    Adema_Sharipova.addToBankAccount(100000)
    print(Adema_Sharipova.displayAccountSum())
    Adema_Sharipova.substractFromBankAccount(110000)
    print(Adema_Sharipova.displayAccountSum())
    print(Adema_Sharipova.moneyConversion(100000, "KZT", "USD"))
    print(Adema_Sharipova.moneyConversion(212.7659574468085, "USD", "KZT"))



main()
