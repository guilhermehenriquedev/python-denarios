import time
import requests
import json
from denarios.core.helpers.criptos import criptos
from denarios.settings.base import * 
from django.db.utils import InterfaceError
from datetime import timedelta

class Exchanges:

    def get_all_cryptos(self, exchanges=None):
        chosen_crypts = criptos()
        for crypto in chosen_crypts:
            print('crypto.....: ', crypto)
            for exchange in exchanges:
                print('Exchange....: ', exchange)
        

    def execute(self):

        _exchanges = [{
                    'binance': BINANCE_API_URL,
                    'brasil_bitcoin': BRASIL_BITCOIN_API_URL,
                    'nova_dax': NOVADAX_API_URL
                    }
                ]

        data = self.get_all_cryptos(exchanges=_exchanges)
        return data


if __name__ == '__main__':
    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()