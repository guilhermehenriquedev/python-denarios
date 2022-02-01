import time
import requests
import json
from denarios.core.helpers.criptos import criptos
from denarios.settings.base import BINACE_API_URL, BINANCE_API_KEY 
from django.db.utils import InterfaceError
from datetime import timedelta

class Exchanges:

    def __init__(self):
       self.headers = {
            'Content-Type': 'application/json'
        } 
    

    def binance(self, headers=None, par_crypt=None):
        
        try:
            url      = BINACE_API_URL + "/api/v3/ticker/price" 
            response = requests.request("GET", url, headers=headers)
            data     = response.json()

        except Exception as err:
            return {'message': 'Erro ao fazer GET'}

        chosen_crypts = criptos(par=par_crypt)

        data = [{
            'no_cripto': item['symbol'],
            'vl_venda': item['price'],
            'vl_compra': item['price']
        } for item in data if item['symbol'] in chosen_crypts]

        return data if data else {'message': 'Sem dados para exibir'} 
   

    def brasil_bitcoin(self, headers=None):
         
        data_brasil_bitcoin = []
        chosen_crypts = criptos()
        for crypto in chosen_crypts:
            try:
                url      = BRASIL_BITCOIN_API_URL + f"/otc/orderbook/{crypto}"
                response = requests.request("GET", url, headers=headers)
                data     = response.json()

                print('data brasil bit....: ', data)

                data_brasil_bitcoin += [{
                    'no_cripto': crypto,
                    'vl_venda': data['sell']['preco'],
                    'vl_compra': data['buy']['preco']
                }]

                print('data....: ', data_brasil_bitcoin)

            except Exception as err:
                data_brasil_bitcoin += [{
                    'no_cripto': crypto,
                    'vl_venda': '--',
                    'vl_compra': '--'
                }]
                continue

        return data_brasil_bitcoin
    
    def bitcoin_trade(self):
        pass

    def nova_dax(self):
        pass

    def mercado_bitcoin(self):
        pass

    def execute(self):

        start_time = time.time()

        binance = self.binance(headers=self.headers, par_crypt='BRL')
        brasil_bitcoin = self.brasil_bitcoin(headers=self.headers)

        data = {
                'binance': binance,
                'brasilbitcoin': brasil_bitcoin 
                }

        elapsed_time = time.time() - start_time
        print(f'Tempo....: {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))}')

        return data 

if __name__ == '__main__':

    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
