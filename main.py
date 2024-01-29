import requests
import pprint
import os
from datetime import date, timedelta


#-------THIS GIVES ME YESTERDAYS INFO --------#
yesterday = date.today() - timedelta(days=1)
response = requests.get(f'https://api.polygon.io/v2/aggs/ticker/X:BTCUSD/range/1/day/{yesterday}/{yesterday}'
                        f'?adjusted=true&sort=asc&limit=120&apiKey={os.environ["polygon_API"]}')
pprint.pprint(response.json())

#-------THIS GIVES BTCUSD LAST 15 MIN---------#
response_now = requests.get('https://blockchain.info/ticker')
pprint.pprint(response_now.json()['USD'])