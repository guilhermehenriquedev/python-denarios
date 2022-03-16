import time
import requests
import json
from denarios.core.helpers.criptos import criptos
from denarios.settings.base import * 
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
            'no_cripto': item['symbol'][:-3],
            'vl_venda': round(float(item['price']), 2),
            'vl_compra': round(float(item['price']), 2)
        } for item in data if item['symbol'] in chosen_crypts]

        return data if data else {'message': 'Sem dados para exibir'} 
   

    def brasil_bitcoin(self, headers=None):
         
        data_brasil_bitcoin = []
        chosen_crypts = criptos()
        for crypto in chosen_crypts:
            print('crypto br......: ', crypto)
            try:
                url      = BRASIL_BITCOIN_API_URL + "/otc/orderbook/" + crypto
                response = requests.request("GET", url, headers=headers)
                data     = response.json()

                data_brasil_bitcoin += [{
                    'no_cripto': crypto,
                    'vl_venda': round(float(data['sell']['preco']), 2),
                    'vl_compra': round(float(data['buy']['preco']), 2)
                }]


            except Exception as err:
                data_brasil_bitcoin += [{
                    'no_cripto': crypto,
                    'vl_venda': 'NDA',
                    'vl_compra': 'NDA'
                }]
                continue

        return data_brasil_bitcoin
    
    def bitcoin_trade(self):
        pass

    def nova_dax(self, headers=None):
        data_novadax = []
        chosen_crypts = criptos()
        for crypto in chosen_crypts:
            try:
                url = NOVADAX_API_URL + f"/market/trades?symbol={crypto}_BRL&limit=2"
                response = requests.request("GET", url, headers=headers)
                data     = response.json()
                data_novadax += [
                    
                ]
                print('data....: ', data)
            except Exception as err:
                continue
        return data_novadax

    def mercado_bitcoin(self):
        pass

    def execute(self):

        start_time = time.time()

        binance = self.binance(headers=self.headers, par_crypt='BRL')
        brasil_bitcoin = self.brasil_bitcoin(headers=self.headers)
        nova_dax = self.nova_dax(headers=self.headers)

        data = {
                'binance': binance,
                'brasilbitcoin': brasil_bitcoin,
                'bitcoin_trade': '',
                'nova_dax': nova_dax
                }

        elapsed_time = time.time() - start_time
        print(f'Tempo....: {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))}')

        return data 

if __name__ == '__main__':

    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
