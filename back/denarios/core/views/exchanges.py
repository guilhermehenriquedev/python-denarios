from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response


class ExchangeViewSet(viewsets.ModelViewSet):
    
    permission_classes = (AllowAny,)
    
    @action(detail=False, methods=['get'], url_path='list')
    def exchange_list(self, request):
        ''' Lista todas as criptomoedas das exchanges '''
        #http://192.168.0.107:8005/integracao/exchanges/criptos/

        if request.method == 'GET':

            return Response(data={'status': 200})
