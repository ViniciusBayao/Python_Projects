import requests

# Simple BRL converter to USD updated using external API

print('-------------BRL--converter -----------------')

# the final currency already setted

final_currency = "USD"

# Function to ask user the amount of money to convert

def ask():
     entry_money = float(input('What is the amount of money you want to convert? '))
     return entry_money

amount = ask()

# Function to get the updated values ​​of the dollar in relation to the BRL, via the external api

def get_v(curr):
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    # url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['USDBRL']['ask']

USD_value = get_v(final_currency)

final = amount / float(USD_value)

print(f'The final value of the conversion between BRL and USD in the updated financial quote is: {final:.2f}')
