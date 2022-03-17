import requests
from denarios.settings.base import * 


class Novadax():

    def execute(self, headers=None, crypto=None):
        data_novadax = []
        try:
            url             = NOVADAX_API_URL + f"/market/trades?symbol={crypto}_BRL&limit=2"
            response        = requests.request("GET", url, headers=headers)
            data            = response.json()
            data_novadax    += [{
                'no_cripto': crypto,
                'vl_venda': 0,
                'vl_compra': 0
            }]
            print('data....: ', data)

        except Exception as err:
            data_brasil_bitcoin += [{
                'no_cripto': crypto,
                'vl_venda': '--',
                'vl_compra': '--'
            }]

        return data_novadax