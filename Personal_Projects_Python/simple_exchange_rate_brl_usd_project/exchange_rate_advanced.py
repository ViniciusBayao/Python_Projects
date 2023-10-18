import requests

def get_fees():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates']

def currency_converter(c_value, c_origin, c_final, fee):
    if c_origin in fee and c_final in fee:
        origin_fee = fee[c_origin]
        final_fee = fee[c_final]
        value_in_usd = c_value / origin_fee
        converted_value = value_in_usd * final_fee
        return converted_value
    else:
        return None

exchange_fee = get_fees()
c_value = float(input('What is the amount to be converted? '))
c_origin = input('What is the source currency? ').upper()
c_final = input('What is the final currency? ').upper()

converted_value = currency_converter(c_value, c_origin, c_final, exchange_fee)

if converted_value is not None:
    print(f'\n{c_value:.2f} {c_origin} correspond to {converted_value:.2f} {c_final}')
else:
    print('Sorry, currency not found or invalid.')
