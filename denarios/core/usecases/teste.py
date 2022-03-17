from email import header
import time
from wsgiref import headers
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
            print('data....: ', data)
            breakpoint()
        except Exception as err:
            return {'message': 'Erro ao fazer GET'}

        chosen_crypts = criptos()

        data = [{
            'no_cripto': item['symbol'][:-3],
            'vl_venda': round(float(item['price']), 2),
            'vl_compra': round(float(item['price']), 2)
        } for item in data if item['symbol'] in chosen_crypts]

        return data if data else {'message': 'Sem dados para exibir'}


    def execute(self):

        chosen_crypts = criptos()
        data_all = []
        for crypto in chosen_crypts:
            data_binance = self.binance(headers=self.headers, par_crypt='BRL')
            

        data = ''
        return data


if __name__ == '__main__':
    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
