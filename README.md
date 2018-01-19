# python-coincap
A python wrapper for the coincap API


## Installation

```
pip install python-coincap
```

## Usage

```
from coincap import CoinCap

coincap = CoinCap()
```

 
#### Get list of all coins
 ```
 coincap.get_all_coins()
 ```
 
##### Response
```
['300', '611', '808', '888', 'INT', 'DTR', 'EOS', 'SANDG', 'QSP'] ...
```

#### Get single coin information
 ```
 coincap.get_coin_detail('BTC')
 ```
 
##### Response
```
{
	'type': 'cmc',
	'volumeAlt': 2757113221.153081,
	'volume': 14833800000,
	'totalCap': 573984069309.739,
	'price_zec': 22.646594468775422,
	'vwap_h24': 11261.792806088255,
	'supply': 16811312,
	'display_name': 'Bitcoin',
	'price_eur': 9273.492114947734,
	'price_usd': 11117.5068749126,
	'price': 11498.8,
	'_id': '179bd7dc-72b3-4eee-b373-e719a9489ed9',
	'market_cap': 193309914425.59998,
	'status': 'available',
	'btcPrice': 11117.5068749126,
	'bitnodesCount': 11695,
	'btcCap': 195365585304.40002,
	'volumeBtc': 3940333743.206316,
	'id': 'BTC',
	'price_btc': 1,
	'volumeTotal': 6697446964.359388,
	'altCap': 378618484005.33685,
	'price_eth': 11.077087606544348,
	'price_ltc': 59.135402527565184,
	'rank': 1,
	'cap24hrChange': 1.9,
	'dom': 58.83
}
```

#### Get coin history

History can be 1, 7, 30, 90, 180, or 365 days
 ```
 coincap.get_coin_history('ETH', 1)
 ```
 
##### Response
```
{
    "market_cap": [
        [
            1504664370000,  
            74300994770     
        ],
        [
            1504750775000,
            74594182198
        ]
    ],
    "price" : [
        [
            1504750775000,
            4507.45 
        ],
        [
            1504839280000,
            4599.26
        ]
    ],
    "volume": [
        [
            1504750775000,  
            2095800000   
        ],
        [
            1504839280000,
            1752760000
        ]
    ]
}
```

#### Get global market information
 ```
 coincap.get_global()
 ```
 
##### Response
```
{
	'altCap': 378618484005.33685,
	'volumeTotal': 6697446964.359388,
	'volumeAlt': 2757113221.153081,
	'btcPrice': 11117.5068749126,
	'dom': 58.83,
	'volumeBtc': 3940333743.206316,
	'btcCap': 195365585304.40002,
	'totalCap': 573984069309.739,
	'bitnodesCount': 11695
}
```

#### Get "front page" coins. (by markert cap rank)
 ```
 coincap.get_front()
 ```
 
##### Response
```
[
    {
        "cap24hrChange": -6.05,
        "long": "Bitcoin",
        "mktcap": 65173805891.25,
        "perc": -6.05,
        "price": 3934.85,
        "shapeshift": true,
        "short": "BTC",
        "supply": 16563225,
        "usdVolume": 2337600000,
        "volume": 2337600000,
        "vwapData": 3997.5639538606733,
        "vwapDataBTC": 3997.5639538606733
    },
    {
        "cap24hrChange": -6.59,
        "long": "Ethereum",
        "mktcap": 26016428866.32,
        "perc": -6.59,
        "price": 275.02,
        "shapeshift": true,
        "short": "ETH",
        "supply": 94598316,
        "usdVolume": 945732000,
        "volume": 945732000,
        "vwapData": 278.03921067242516,
        "vwapDataBTC": 278.03921067242516
    }
]
```

#### Get coin symbols, names, and aliases
 ```
 coincap.get_map()
 ```
 
##### Response
```
{
	'aliases': [],
	'name': 'Ethereum',
	'symbol': 'ETH'
}, 
{
	'aliases': [],
	'name': 'Bitz',
	'symbol': 'BITZ'
}, 
{
	'aliases': [],
	'name': 'OKCash',
	'symbol': 'OK'
}
```

