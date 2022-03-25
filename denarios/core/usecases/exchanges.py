from urllib import response
import requests
from denarios.core.helpers.criptos import criptos
from denarios.settings.base import * 
from django.db.utils import InterfaceError
from datetime import timedelta

class Exchanges:

    def __init__(self, api_key=None):
        
        self.headers = {
            'Content-Type': 'application/json'
        }

    def binance(self, headers=None, par_crypt=None, crypt=None):

        try:
            crypt_get = crypt + par_crypt
            url      = BINACE_API_URL + f"/api/v3/ticker/price?symbol={crypt_get}" 
            response = requests.request("GET", url, headers=headers)
            data     = response.json()

            data_binance = {
                'exchange': 'Binance',
                'vl_venda': round(float(data['price']), 2),
                'vl_compra': round(float(data['price']), 2)
            } 

        except Exception as err:
            data_binance = {
                'exchange': 'Binance',
                'vl_venda': 'Indisponível',
                'vl_compra': 'Indisponível'
            } 

        return data_binance 
   
    def brasil_bitcoin(self, headers=None, crypt=None):
        
        try:
            url      = BRASIL_BITCOIN_API_URL + "/otc/orderbook/" + crypt
            response = requests.request("GET", url, headers=headers)
            data     = response.json()

            data_brasil_bitcoin = {
                'exchange': 'Brasil Bitcoin',
                'vl_venda': round(float(data['sell']['preco']), 2),
                'vl_compra': round(float(data['buy']['preco']), 2)
            }

        except Exception as err:
            data_brasil_bitcoin = {
                'Exchange': 'Brasil Bitcoin',
                'vl_venda': 'Indisponível',
                'vl_compra': 'Indisponível'
            }

        return data_brasil_bitcoin
    
    def nova_dax(self, headers=None, par_crypt=None, crypt=None):
        
        crypt_get = crypt + "_" + par_crypt
        
        try:
            url = NOVADAX_API_URL + f"/market/depth?symbol={crypt_get}"
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            
            data_nova_dax = {
                'Exchange': 'Nova Dax',
                'vl_venda': round(float(data['data']['asks'][0][0]), 2),
                'vl_compra': round(float(data['data']['bids'][0][0]), 2)
            }
            
        except Exception as err:
            data_nova_dax = {
                'Exchange': 'Nova Dax',
                'vl_venda': 'Indisponível',
                'vl_compra': 'Indisponível'
            }
        
        return data_nova_dax

    def bitcoin_trade(self, headers=None, par_crypt=None, crypt=None):
        
        crypt_get = par_crypt + crypt
        try:
            url = BITCOIN_TRADE_API_URL + f"public/{crypt_get}/ticker?x-api-key=U2FsdGVkX19hx5WwkPxaLUB8vHGGbFWJNvCGY1yne9jwy9tgGxC6AWWnHkHVyxr0"
            response = requests.request("GET", url, headers=headers)
            data = response.json()
            
            print('data bitcoin trade *******', data)
            
        except Exception as err:
            print('******Error')
        
    def mercado_bitcoin(self, headers=None, crypt=None):
        pass

    def execute(self):

        chosen_crypts = criptos() 
        data = []
        for crypt in chosen_crypts:
            binance = self.binance(headers=self.headers, par_crypt='BRL', crypt=crypt)
            brasil_bitcoin = self.brasil_bitcoin(headers=self.headers, crypt=crypt)
            nova_dax = self.nova_dax(headers=self.headers, par_crypt='BRL', crypt=crypt)
            bitcoin_trade = self.bitcoin_trade(headers=self.headers, par_crypt='BRL', crypt=crypt)
            
            data += [{crypt: [binance, brasil_bitcoin, nova_dax,]}]

        return data 

if __name__ == '__main__':

    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
