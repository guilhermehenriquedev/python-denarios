from denarios.core.helpers.criptos import criptos
from denarios.core.usecases.exchanges_cryptos.brasil_bitcoin import BrasilBitcoin
from denarios.core.usecases.exchanges_cryptos.nova_dax import Novadax

class Exchanges:

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def execute(self):
        chosen_crypts = criptos()
        data_all = []
        for crypto in chosen_crypts:
            data_brasil_bitcoin = BrasilBitcoin().execute(headers=self.headers, crypto=crypto)
            data_nova_dax = Novadax().execute(headers=self.headers, crypto=crypto)
            data_binance 

            #data_all += data_brasil_bitcoin
        return 'data_all'


if __name__ == '__main__':
    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    list_exchanges.execute()
