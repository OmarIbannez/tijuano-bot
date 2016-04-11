from currency import Currency
from datetime import datetime


currency = Currency('2016-04-07', 'USD', ['MXN', 'EUR'])
c = currency.fetch()

print(c)
