# Converting computational numerical bases

print('-' * 50, 'Program for converting computational numerical bases', '-' * 50)


def init_base():
    print('-' * 20, 'Menu', '-' * 20)
    base_init = int(input('Select an initial base option for an input numeric value.'
                          '\n1- Decimal'
                          '\n2- Binary'
                          '\n3- Octal'
                          '\n4- Hexadecimal'
                          '\nEnter the number corresponding to the desired initial base above: '))
    return base_init


def get_number(base_i):
    if base_i == 1:
        try:
            dec_num = int(input("Enter the value in decimal: "))
            print(f'Input value in decimal: {dec_num}')
            return dec_num
        except ValueError:
            print('Please, insert only one decimal value.')
    if base_i == 2:
        try:
            binary_num = int(input("Enter the value in binary: "), 2)
            print(f'Input value in binary: {bin(binary_num):.2f}')
            return binary_num
        except ValueError:
            print('Please, insert only one binary value.')
    if base_i == 3:
        try:
            octal_num = int(input("Enter the value in octal: "), 8)
            print(f'Input value in octal: {oct(octal_num):.2f}')
            return octal_num
        except ValueError:
            print('Please, insert only one octal value.')
    if base_i == 4:
        try:
            hexad_num = int(input("Enter the value in hexadecimal: "), 16)
            print(f'Input value in hexadecimal: {hex(hexad_num):.2f}')
            return hexad_num
        except ValueError:
            print('Please, insert only one hexadecimal value.')


def final_base():
    print('-' * 20, 'Menu', '-' * 20)
    base_end = int(input('Select an initial base option for an input numeric value.'
                         '\n1- Decimal'
                         '\n2- Binary'
                         '\n3- Octal'
                         '\n4- Hexadecimal'
                         '\nEnter the number corresponding to the desired final base above: '))
    return base_end


def converter(bi, be, n):
    if bi == be:
        return f'The initial base value {bi}, is equal to the final base value: {be}'
    if be == 1:
        return f'Final base conversion value: {n}'
    if bi == 1 and be == 2:
        return f'Final base conversion value: {bin(n)}'
    if bi == 1 and be == 3:
        return f'Final base conversion value: {oct(n)}'
    if bi == 1 and be == 4:
        return f'Final base conversion value: {hex(n)}'
    if bi == 2 and be == 3:
        return f'Final base conversion value: {oct(n)}'
    if bi == 2 and be == 4:
        return f'Final base conversion value: {hex(n)}'
    if bi == 3 and be == 2:
        return f'Final base conversion value: {bin(n)}'
    if bi == 3 and be == 4:
        return f'Final base conversion value: {hex(n)}'
    if bi == 4 and be == 2:
        return f'Final base conversion value: {bin(n)}'
    if bi == 4 and be == 3:
        return f'Final base conversion value: {oct(n)}'


first_base = init_base()
num = get_number(first_base)
final_base = final_base()
conversion_number = converter(first_base, final_base, num)
print(conversion_number)
