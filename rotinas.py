import requests

def loadDados(index=''):
    dados = requests.get('https://raw.githubusercontent.com/grovina/assisnet/master/casmurro.txt').text
    conteudo = []
    return conteudo