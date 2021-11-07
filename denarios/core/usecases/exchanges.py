import requests
import json
from denarios.core.helpers.criptos import criptos
from denarios.settings import BINACE_API_URL, BINANCE_API_KEY 
from django.db.utils import InterfaceError

class Exchanges:
    
    def binance(self, headers=None):
        
        prices_criptos = []
        for name_cripto in criptos:

            try:
            
                name_cripto  = name_cripto + 'BTC'
                url          = BINACE_API_URL + f"/sapi/v1/margin/priceIndex?symbol={name_cripto}"
                response     = requests.request("GET", url, headers=headers)
                data         = response.json()

                preco_compra = data.get('price')

                payload = {
                    "no_cripto": name_cripto,
                    "vl_compra": preco_compra
                    } 

                prices_criptos.append(payload)

            except Exception as err:
                print(f'Falha ao fazer GET da moeda...: {name_cripto}')
                continue

        payload_binance = {"binance": prices_criptos}
        return payload_binance 


    def execute(self):

        headers = {
            'Content-Type': 'application/json',
            'X-MBX-APIKEY': BINANCE_API_KEY 
        }

        binance = self.binance(headers=headers)

        exchanges = [binance,] 
        return exchanges

if __name__ == '__main__':

    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
