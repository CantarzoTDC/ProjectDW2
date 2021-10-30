import requests, json
from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from typing import List, Any
from rotinas import loadDados
app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['get', 'post'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/pesquisa', methods=['get'])
def getCard():
    q = request.form.get('q')
    if (q == ''):
        dados = requests.get('https://api.scryfall.com/cards/search?format=json&include_extras=false&include_multilingual=false&order=cmc&page=1&q=c%3C=wbgru&unique=cards&pretty=true').json()
    else:
        dados = requests.get('https://api.scryfall.com/catalog/card/search?q='+q+'&format=json&pretty=true').json()

    nome:str = dados['data'][0]['name']
    imguri = dados['data'][0]['image_uris']['normal']
    idioma:str = dados['data'][0]['lang']
    custo_m:str = dados['data'][0]['mana_cost']
    cmc:str = dados['data'][0]['cmc']
    p_r:str = (dados['data'][0]['power'] + '/' + dados['data'][0]['toughness'])
    cor:str = dados['data'][0]['colors']
    refs = dados['data'][0]['related_uris']['gatherer']
    more = dados['has_more']
    if more == True:
        nxt = dados['next_page']
    else:
        nxt = ''

    return render_template('pesquisa.html')


@app.route('/NAMEme', methods=['get', 'post'])
def nameMe():
    return 'please'


if __name__ == '__main__':
    app.run(debug=True)
