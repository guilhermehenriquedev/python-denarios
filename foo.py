import requests



def test_get():
    # Define a URL da API da Brasil Bitcoin
    url = 'https://api.brasilbitcoin.com.br/v3/public/'

    # Faz uma solicitação para obter as informações de compra e venda de todas as criptomoedas disponíveis
    response = requests.get(url + 'ticker')

    if response.status_code == 200:
        # Se a solicitação foi bem-sucedida, extrai as informações de compra e venda de cada criptomoeda
        data = response.json()
        for symbol in data.keys():
            if symbol != 'brl':
                bid = data[symbol]['buy']
                ask = data[symbol]['sell']
                print(f'{symbol}:\n- Compra: {bid}\n- Venda: {ask}\n')
    else:
        print('Falha na solicitação')
    
