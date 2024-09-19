import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                'top_ask': {'price': 121.2, 'size': 36},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109},
                'id': '0.109974697771',
                'stock': 'ABC'
            },
            {
                'top_ask': {'price': 121.68, 'size': 4},
                'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 117.87, 'size': 81},
                'id': '0.109974697771',
                'stock': 'DEF'
            }
        ]
        """ ------------ Add the assertion below ------------ """

        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, 120.84))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.775))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, 119.84))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, 119.775))

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_calculatePriceBidEqualAsk(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 121.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 121.2, 121.2, 121.2))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 121.68, 121.68, 121.68))

    def test_getRatio(self):
        self.assertEqual(getRatio(10, 5), 2)
        self.assertEqual(getRatio(10, 0), None)
        self.assertEqual(getRatio(0, 5), 0)
        self.assertEqual(getRatio(0, 0), None)


if __name__ == '__main__':
    unittest.main()
