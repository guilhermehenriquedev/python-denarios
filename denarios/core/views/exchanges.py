import time
import asyncio
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
#from denarios.core.usecases.exchanges_copy import Exchanges
from denarios.core.usecases.exchanges import Exchanges


class ExchangeViewSet(viewsets.ModelViewSet):

    permission_classes = (AllowAny,)
    
    @action(detail=False, methods=['get'], url_path='list')
    def exchange_list(self, request):
        ''' Lista todas as criptomoedas das exchanges '''
        # http://192.168.0.108:8005/api/exchanges/list/

        if request.method == 'GET':
            
            start_time = time.time()
            print(f'Iniciando {start_time}')
            
            list_exchanges = Exchanges()
            #data = asyncio.run(list_exchanges.execute())
            data = list_exchanges.execute()

            elapsed_time = time.time() - start_time
            print(f'Tempo decorrido: {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))}')
            return Response(data={'data': data}, status=status.HTTP_200_OK)
