from typing import List, Dict
from time import sleep

from models.product import Product
from utils.helper import format_float_str_coin

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('-' * 40)
    print('Welcome'.center(40, '-'))
    print('Geek Shop'.center(40, '-'))
    print('-' * 40)

    print('Select and option below: ')
    print('1- Register product')
    print('2- list products')
    print('3- Buy products')
    print('4- View cart')
    print('5- Finish order')
    print('6- Exit system')

    opt: int = int(input())

    if opt == 1:
        register_product()
    elif opt == 2:
        list_products()
    elif opt == 3:
        buy_product()
    elif opt == 4:
        view_cart()
    elif opt == 5:
        finish_order()
    elif opt == 6:
        print('Come back anytime!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option.')
        sleep(1)
        menu()


def register_product() -> None:
    print('Product register: ')
    print('-' * 40)

    name: str = input("Input the product's name: ")
    price: float = float(input("Input the product's price: "))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The product {product.name} was successfully registered!')
    sleep(2)
    menu()


def list_products() -> None:
    if len(products) > 0:
        print('Products list: ')
        print('-' * 40)
        for product in products:
            print(product)
            print('-' * 40)
            sleep(1)
    else:
        print('There are no registered products yet.')
    sleep(2)
    menu()


def buy_product() -> None:
    if len(products) > 0:
        print('Input the product code you want to add to bag: ')
        print('-' * 40)
        print('Products available'.center(40, '-'))
        for product in products:
            print(product)
            print('-' * 40)
            sleep(1)
        code: int = int(input())

        product: Product = get_product_by_code(code)

        if product:
            if len(cart) > 0:
                have_in_cart: bool = False
                for item in cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] = quant + 1
                        print(f'The product {product.name} now has {quant + 1} units in the cart.')
                        have_in_cart = True
                        sleep(2)
                        menu()
                if not have_in_cart:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product {product.name} has been successfully added to the cart.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} has been successfully added to the cart.')
                sleep(2)
                menu()
        else:
            print(f'The product with code {code} was not found.')
        sleep(2)
        menu()
    else:
        print('There are no products to sell yet.')
        sleep(2)
        menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('Products in the cart: ')
        print('-' * 40)
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('-' * 40)
                sleep(1)
    else:
        print('There are no products to sell yet.')
        sleep(2)
        menu()


def finish_order() -> None:
    if len(cart) > 0:

        total_value: float = 0

        print('Products in cart: ')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                total_value += data[0].price * data[1]
                print('-' * 40)
                sleep(1)
        print(f'Your invoice is: ${format_float_str_coin(total_value)}')
        print('Come back anytime!')
        cart.clear()
        sleep(5)
    else:
        print('No products have been added to the cart yet.')
        sleep(2)
        menu()


def get_product_by_code(code: int) -> Product:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p


if __name__ == '__main__':
    main()
