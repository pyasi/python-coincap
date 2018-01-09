import requests
import json

BASE_URL = 'http://coincap.io/'


class CoinCap(object):

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def _query_coincap(self, endpoint):
        """

        :param endpoint:
        :return:
        """
        response = requests.get(self.base_url + endpoint)

        if response.status_code != 200:
            raise Exception('The server has responded with an error')
        response = json.loads(response.text)
        return response

    def get_all_coins(self):
        """

        """
        return self._query_coincap('coins/')

    def get_map(self):
        """

        """
        return self._query_coincap('map/')

    def get_front(self):
        """

        """
        return self._query_coincap('front/')

    def get_global(self):
        """

        """
        return self._query_coincap('global/')

    def get_coin_detail(self, coin_ticker):
        """

        :param ticker:
        :return:
        """
        return self._query_coincap('page/{}'.format(coin_ticker))

    def get_coin_history(self, coin_ticker, days):
        """

        :param coin_ticker:
        :param days:
        :return:
        """
        supported_days = [1, 7, 30, 90, 180, 365]
        if days not in supported_days:
            raise Exception('{} days not supported, please pick from {}'.format(days, supported_days))
        return self._query_coincap('history/{}day/{}'.format(str(days), coin_ticker))
