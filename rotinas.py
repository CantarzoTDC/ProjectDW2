from flask import request
import requests
import json

def loadDados(index=''):
    url = 'https://api.scryfall.com/cards/search?q=platinum'
    dados = requests.get(url).json()
    dados_b = dados['data'][0]
    '''group_barq = [
        barq['data'][0]['name'],
        barq['data'][0]['image_uris']['normal'],
        barq['data'][0]['lang'],
        barq['data'][0]['mana_cost'],
        barq['data'][0]['cmc'],
        barq['data'][0]['power'],
        barq['data'][0]['toughness'],
        barq['data'][0]['colors'],
        barq['data'][0]['related_uris']['gatherer']
    ]'''


    dados = requests.get('https://raw.githubusercontent.com/grovina/assisnet/master/casmurro.txt').text
    conteudo = []
    for d in dados:
        nome = dados['data'][0]['name']
        imgurl = dados['data'][0]['image_uris']['normal']
        idioma = dados['data'][0]['lang']
        custo = dados['data'][0]['mana_cost']
        cmc = dados['data'][0]['cmc']
        poder = dados['data'][0]['power']
        resist = dados['data'][0]['toughness']
        cor = dados['data'][0]['colors']
        mtg_url = dados['data'][0]['related_uris']['gatherer']
    return conteudo