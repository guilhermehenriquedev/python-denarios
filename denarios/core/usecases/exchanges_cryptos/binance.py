import requests
from denarios.settings.base import * 


class Binance:

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