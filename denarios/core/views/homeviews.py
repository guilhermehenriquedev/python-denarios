from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.http import JsonResponse
import requests, json


def index(request):

    return render(request, "index.html", {
        'debug':settings.DEBUG,
        'environment':settings.ENVIRONMENT
        })

def painel(request):
    return render(request, "painel.html", {
        'debug':settings.DEBUG,
        'environment':settings.ENVIRONMENT})

def error_teste(request):
    raise Exception("Teste de erro (debug) - manda email")
