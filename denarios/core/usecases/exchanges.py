from django.http import JsonResponse
import requests
import asyncio
from denarios.core.helpers.criptos import criptos
from denarios.settings.base import *
from aiohttp import ClientSession


class Exchanges:
    ''' Chama as exchanges e faz a acao de consulta dos valores '''

    async def binance(self, par_crypt=None, crypt=None):

        print('binance...: ', crypt)

        crypt_get = crypt + par_crypt
        url = BINACE_API_URL + f"/api/v3/ticker/price?symbol={crypt_get}"

        try:
            async with ClientSession() as session:
                async with session.get(url) as response:

                    data = await response.json()
                    data_binance = {
                        'exchange': 'Binance',
                        'vl_venda': round(float(data['price']), 2),
                        'vl_compra': round(float(data['price']), 2)
                    }

        except Exception as err:
            data_binance = {
                'exchange': 'Binance',
                'vl_venda': 0.00,
                'vl_compra': 0.00
            }
            pass

        return data_binance

    async def brasil_bitcoin(self, crypt=None):

        print('bitcoin...: ', crypt)

        try:
            url = BRASIL_BITCOIN_API_URL + "/otc/orderbook/" + crypt
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    data_brasil_bitcoin = {
                        'exchange': 'Brasil Bitcoin',
                        'vl_venda': round(float(data['sell']['preco']), 2),
                        'vl_compra': round(float(data['buy']['preco']), 2)
                    }

        except Exception as err:
            data_brasil_bitcoin = {
                'exchange': 'Brasil Bitcoin',
                'vl_venda': 0.00,
                'vl_compra': 0.00
            }
            pass

        return data_brasil_bitcoin

    async def nova_dax(self, par_crypt=None, crypt=None):

        print('novadax...: ', crypt)
        crypt_get = crypt + "_" + par_crypt
        try:
            url = NOVADAX_API_URL + f"/market/depth?symbol={crypt_get}"
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    data_nova_dax = {
                        'exchange': 'Nova Dax',
                        'vl_venda': round(float(data['data']['asks'][0][0]), 2),
                        'vl_compra': round(float(data['data']['bids'][0][0]), 2)
                    }

        except Exception as err:
            print('ERRO NOVA DAX ****** ', err)
            data_nova_dax = {
                'exchange': 'Nova Dax',
                'vl_venda': 0.00,
                'vl_compra': 0.00
            }
            pass

        return data_nova_dax


    async def mercado_bitcoin(self, crypt=None):
        
        print('mercado bitcoint...:', crypt)
        try:
            url = MERCADO_BITCOIN_API_URL + f"/{crypt}/ticker/"
            async with ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    data_mercado_bitcoin = {
                        'exchange': 'Mercado Bitcoin',
                        'vl_venda': round(float(data['ticker']['sell']), 2),
                        'vl_compra': round(float(data['ticker']['buy']), 2)
                    }

        except Exception as err:
            print('ERRO MERCADO BITCOIN ****** ', err)
            data_mercado_bitcoin = {
                'exchange': 'Mercado Bitcoin',
                'vl_venda': 0.00,
                'vl_compra': 0.00
            }
            pass

        return data_mercado_bitcoin

    async def execute(self):

        chosen_crypts = criptos()
        data = []

        for crypt in chosen_crypts:

            binance = self.binance(par_crypt='BRL', crypt=crypt)
            brasil_bitcoin = self.brasil_bitcoin(crypt=crypt)
            nova_dax = self.nova_dax(crypt=crypt, par_crypt='BRL')
            mercado_bitcoin = self.mercado_bitcoin(crypt=crypt)

            await asyncio.wait([
                binance,
                brasil_bitcoin,
                nova_dax,
                mercado_bitcoin
            ])

            #data += [{crypt: [binance, brasil_bitcoin]}]
            
        return data


if __name__ == '__main__':

    import asyncio
    from denarios.core.usecases.exchanges import Exchanges
    list_exchanges = Exchanges()
    asyncio.run(list_exchanges.execute())
