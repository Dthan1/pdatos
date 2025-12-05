import requests
from pprint import pprint

url= "https://data-api.binance.vision/api/v3/ticker/price"

response= requests.get(url)
if response.status_code == 200:
    print("Éxito!")
else:
    print("Error:", response.status_code)


data= response.json()

#type(data)
#dato = "symbol"
n=0
while(True):

    if(data[n]['symbol']=="BTCUSD"):
        pprint(data[n]['symbol'] +" Precio:"+ data[n]['price'])
        break
    else:
        n=n+1
