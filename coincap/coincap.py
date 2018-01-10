import requests
import json

BASE_URL = 'http://coincap.io/'


class CoinCap(object):
    """
    Object to interact with coincap API
    """

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def _query_coincap(self, endpoint):
        """
        Hits the coincap.io endpoint

        :param endpoint: endpoint to hit
        :return: response as JSON
        """
        response = requests.get(self.base_url + endpoint)

        if response.status_code != 200:
            raise Exception('The server has responded with an error')
        response = json.loads(response.text)
        return response

    def get_all_coins(self):
        """
        Returns list of all coin tickers
        """
        return self._query_coincap('coins/')

    def get_map(self):
        """
        Returns JSON object of Coin symbols/names and known aliases
        """
        return self._query_coincap('map/')

    def get_front(self):
        """
        Returns JSON object of the top coins
        """
        return self._query_coincap('front/')

    def get_global(self):
        """
        Return global data of the crypto market
        """
        return self._query_coincap('global/')

    def get_coin_detail(self, coin_ticker):
        """
        Returns details for a specific coin, must use the ticket

        :param coin_ticker: ticker for coin to get detail from
        :return: JSON object of coin's details
        """
        return self._query_coincap('page/{}'.format(coin_ticker))

    def get_coin_history(self, coin_ticker, days):
        """
        Returns the history of a coin

        :param coin_ticker: ticker for coin to get detail from
        :param days: number of days to receive history from. Must be one of [1, 7, 30, 90, 180, 365]
        :return: JSON object with coin's history
        """
        supported_days = [1, 7, 30, 90, 180, 365]
        if days not in supported_days:
            raise Exception('{} days not supported, please pick from {}'.format(days, supported_days))
        return self._query_coincap('history/{}day/{}'.format(str(days), coin_ticker))
