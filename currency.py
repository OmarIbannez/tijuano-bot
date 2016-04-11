from settings import DOLLAR_API_URL
import requests


class Currency:

    def __init__(self, date, base, symbols):
        self.date = date
        self.base = base
        self.symbols = symbols

    def fetch(self):
        data = {'base': self.base, 'symbols': ",".join(self.symbols)}
        url = DOLLAR_API_URL + self.date
        response = requests.get(url, data=data)

        response.raise_for_status()

        return response.json()
