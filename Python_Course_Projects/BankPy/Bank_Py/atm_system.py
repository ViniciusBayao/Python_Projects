"""
Project 3 - Simple Bank System

Description:

We must develop an application, which, when initialized, asks the user to choose what it wants to do in the bank,
how to create an account, make a withdrawal, make a deposit, make a transfer, list accounts or exit the system.

"""
from typing import List
from time import sleep

from models.customer import Customer
from models.account import Account

accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('-' * 40)
    print('ATM'.center(40, '-'))
    print('Geek Bank'.center(40, '-'))
    print('-' * 40)

    print('Select an option below:')
    print('1- Create Account ')
    print('2- Make a Withdraw')
    print('3- Make a Deposit')
    print('4- Make transfer')
    print('5- list accounts')
    print('6- Exit the system')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Come back anytime!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option.')
        sleep(2)
        menu()


def create_account() -> None:

    print('Enter customer data: ')

    name: str = input("Customer's name: ")
    email: str = input("Customer's email: ")
    ssn: str = input("Customer's SSN: ")
    birth_date: str = input("Customer's day of birth: ")

    customer: Customer = Customer(name, email, ssn, birth_date)

    account: Account = Account(customer)

    accounts.append(account)

    print('Account created with success!')
    print('Account data: ')
    print('-' * 40)
    print(account)
    sleep(2)
    menu()


def withdraw() -> None:
    if len(accounts) > 0:
        number: int = int(input('Provide your account number: '))

        account: Account = search_accounts_by_number(number)

        if account:
            value: float = float(input('Enter withdrawal amount: '))

            account.withdraw(value)
        else:
            print(f'No account found with number: {number}.')
    else:
        print('There are no registered accounts yet.')
    sleep(2)
    menu()


def deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input('Provide your account number: '))

        account: Account = search_accounts_by_number(number)

        if account:
            value: float = float(input('Enter deposit amount: '))

            account.deposit(value)
        else:
            print(f'No account found with number: {number}')
    else:
        print('There are no registered accounts yet.')
    sleep(2)
    menu()


def transfer() -> None:
    if len(accounts) > 0:
        number_o: int = int(input('Provide your account number: '))

        account_o: Account = search_accounts_by_number(number_o)

        if account_o:
            number_d: int = int(input('Enter the destination account number: '))

            account_d: Account = search_accounts_by_number(number_d)

            if account_d:
                value: float = float(input('Enter the amount of the bank transfer : '))

                account_o.transfer(account_d, value)
            else:
                print(f'The destination account, with number {number_d} was not found.')
        else:
            print(f'Your account number {number_o} was not found.')
    else:
        print('There are no registered accounts yet.')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('Account listing: ')

        for account in accounts:
            print(account)
            print('-' * 40)
            sleep(1)
    else:
        print('There are no registered accounts.')
    sleep(2)
    menu()


def search_accounts_by_number(number: int) -> Account:
    c: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.number == number:
                c = account
    return c


if __name__ == '__main__':
    main()
