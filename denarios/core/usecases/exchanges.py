import requests
import json
from denarios.core.helpers.criptos import criptos
from denarios.settings import BINACE_API_URL, BINANCE_API_KEY 

class Exchanges:
    
    def binance(self, payload=None, headers=None):
        
        prices_criptos = []
        for name_cripto in criptos:
            
            name_cripto = name_cripto + 'BTC'
            url = BINACE_API_URL + f"/sapi/v1/margin/priceIndex?symbol={name_cripto}"

            response = requests.request("GET", url, headers=headers, data=payload)
            data = response.json()
            print('data....: ', data)
            
            #TODO: Fazer com que o payload venha dessa forma, caso nao tenha valor no request pegue um default
            '''
            prices_criptos += {
                    'no_cripto': data['symbol'],
                    'vl_compra': data['price']
                    } 
            '''

        return prices_criptos 


    def execute(self):

        payload={}
        headers = {
            'Content-Type': 'application/json',
            'X-MBX-APIKEY': BINANCE_API_KEY 
        }

        binance = self.binance(payload=payload, headers=headers)
        
        print('binance....: ', binance)

if __name__ == '__main__':

    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
