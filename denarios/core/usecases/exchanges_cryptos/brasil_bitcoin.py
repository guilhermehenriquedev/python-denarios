import requests
from denarios.settings.base import * 

class BrasilBitcoin:

    def execute(self, headers=None, crypto=None):
         
        data_brasil_bitcoin = []
        try:
            url      = BRASIL_BITCOIN_API_URL + "/otc/orderbook/" + crypto
            response = requests.request("GET", url, headers=headers)
            data     = response.json()

            data_brasil_bitcoin = [{
                'no_cripto': crypto,
                'vl_venda': round(float(data['sell']['preco']), 2),
                'vl_compra': round(float(data['buy']['preco']), 2)
            }]

        except Exception as err:
            data_brasil_bitcoin += [{
                'no_cripto': crypto,
                'vl_venda': '--',
                'vl_compra': '--'
            }]
        return data_brasil_bitcoin