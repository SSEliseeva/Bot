import requests
import json

from Config1 import keys

class ConvertionExeption(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote = str, base = str, amount = str):

        if quote == base:
            raise ConvertionExeption('Невозможно перевести одинаковые валюты')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Не удалось обработать {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base * amount
