import requests
import json

def get_cotacao_dollar():
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    cotacao = cotacao.json
    return cotacao["USDBRL"]["bid"]

