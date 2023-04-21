from datetime import (
    date,
    datetime
)


def date_to_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_to_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_coin(value: float) -> str:
    return f'R$ {value:,.2f}'
