from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from denarios.core.usecases.exchanges import Exchanges


class ExchangeViewSet(viewsets.ModelViewSet):
    
    permission_classes = (AllowAny,)
    
    @action(detail=False, methods=['get'], url_path='list')
    def exchange_list(self, request):
        ''' Lista todas as criptomoedas das exchanges '''
        #http://192.168.0.108:8005/api/exchanges/list/

        if request.method == 'GET':

            list_exchanges = Exchanges()
            data = list_exchanges.execute()
            return Response(data={'data':data})
