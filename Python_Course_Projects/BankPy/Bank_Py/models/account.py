from guppe.Bank_Py.models.customer import Customer
from guppe.Bank_Py.utils.helper import format_float_str_coin


class Account:

    code: int = 1001

    def __init__(self, customer: Customer) -> None:
        self.__number: int = Account.code
        self.__customer: Customer = customer
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total_balance: float = self._calculate_total_balance
        Account.code += 1

    def __str__(self) -> str:
        return f'Account number: {self.number} \nCustomer: {self.customer.name} \nTotal balance: ' \
               f'{format_float_str_coin(self.total_balance)}'

    @property
    def number(self) -> int:
        return self.__number

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def _calculate_total_balance(self) -> float:
        return self.balance + self.limit

    def deposit(self, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._calculate_total_balance
            print('Deposit made successfully!')
        else:
            print('Error when making deposit. Try again.')

    def withdraw(self, value: float) -> None:
        if (value > 0) and (self.total_balance >= value):
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.limit + remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance
            print('Withdrawal made successfully!')
        else:
            print('Withdrawal not performed. Try again!')

    def transfer(self, final: object, value: float) -> None:
        if (value > 0) and (self.total_balance >= value):
            if self.balance >= self.balance:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
                final.balance = final.balance + value
                final.total_balance = final._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.balance = 0
                self.limit = self.limit + remaining
                self.total_balance = self._calculate_total_balance
                final.balance = final.balance + value
                final.total_balance = final._calculate_total_balance
            print('Transfer performed successfully!')
        else:
            print('Transfer failed. Try again!')
