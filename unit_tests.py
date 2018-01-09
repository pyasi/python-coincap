from coincap.coincap import *
import unittest


class TestCoinCap(unittest.TestCase):
    """

    """

    def setUp(self):
        self.coin_cap = CoinCap()

    def test_history_failure(self):
        with self.assertRaises(Exception):
            self.coin_cap.get_coin_history('BTC', 9)

    def test_history_success(self):
        response = self.coin_cap.get_coin_history('ETH', 7)
        assert isinstance(response, dict)

    def test_coin_detail(self):
        response = self.coin_cap.get_coin_detail('BTC')
        assert isinstance(response, dict)

    def test_global(self):
        response = self.coin_cap.get_global()
        assert isinstance(response, dict)

    def test_map(self):
        response = self.coin_cap.get_map()
        assert isinstance(response, list)
        assert all(isinstance(item, dict) for item in response)

    def test_get_all_coins(self):
        response = self.coin_cap.get_all_coins()
        assert isinstance(response, list)
        assert all(isinstance(item, str) for item in response)

    def test_get_front(self):
        response = self.coin_cap.get_front()
        assert isinstance(response, list)
        assert all(isinstance(item, dict) for item in response)


if __name__ == "__main__":
    unittest.main()