from datetime import date
from guppe.Bank_Py.utils.helper import date_to_str, str_to_date


class Customer(object):

    count: int = 101

    def __init__(self: object, name: str, email: str, ssn: str, birth_date: str) -> None:
        self.__code: int = Customer.count
        self.__name: str = name
        self.__email: str = email
        self.__ssn: str = ssn
        self.__birth_date: date = str_to_date(birth_date)
        self.__register_date: date = date.today()
        Customer.count += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def ssn(self: object) -> str:
        return self.__ssn

    @property
    def birth_date(self: object) -> date:
        return date(self.__birth_date)

    @property
    def register_date(self: object) -> date:
        return date(self.__register_date)

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nNome: {self.name} \nData de Nascimento: {self.birth_date} ' \
               f'\nRegister: {self.register_date}'
