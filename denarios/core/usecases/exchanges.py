import requests
from denarios.core.helpers.criptos import criptos
from denarios.settings.base import * 
from django.db.utils import InterfaceError
from datetime import timedelta

class Exchanges:

    def __init__(self):
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
    
    def nova_dax(self, headers=None, crypt=None):
        pass

    def mercado_bitcoin(self):
        pass

    def bitcoin_trade(self):
        pass

    def execute(self):

        chosen_crypts = criptos() 
        data = []
        for crypt in chosen_crypts:
            binance = self.binance(headers=self.headers, par_crypt='BRL', crypt=crypt)
            brasil_bitcoin = self.brasil_bitcoin(headers=self.headers, crypt=crypt)

            data += [{crypt: [binance, brasil_bitcoin,]}]

        return data 

if __name__ == '__main__':

    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
