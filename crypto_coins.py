from datetime import datetime
from pprint import pprint
import requests


base_url = 'https://api.coingecko.com/api/v3/coins'


def fetch_coin_price(coin_id):
    url = '{}/{}'.format(base_url, coin_id)
    response = requests.get(url)

    #checks if request succeeded
    if response.status_code == 200:
        body = response.json()
        return body['tickers'][0]['converted_last']['usd']

    return 0.0


def get_prices(portfolio):
    prices = {}

    for coin in portfolio:
        prices[coin] = fetch_coin_price(coin)

    return prices


if __name__ == '__main__':
    portfolio = ['bitcoin', 'ethereum', 'litecoin',
                 'monero', 'ripple', 'iota']

    prices = get_prices(portfolio)
    now = datetime.now()
    date = '{}/{}/{} | {}:{}'.format(now.day, now.month,
                                     now.year, now.hour, now.minute)

    print('\n*** Coins market value in USD: {} ***\n'.format(date))
    pprint(prices)
