import requests, json
from flask import Flask, render_template, request, jsonify
from typing import List, Any
from rotinas import loadDados
app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/search', methods=['get'])
def getCard():
    q = request.form.get('search')
    dados = requests.get('https://api.scryfall.com/catalog/card/search?q='+q)

    d for d in dados:
        nome = dados['data'][0]['name']
        imgurl = dados['data'][0]['image_uris']['normal']
        idioma = dados['data'][0]['lang']
        custo = dados['data'][0]['mana_cost']
        cmc = dados['data'][0]['cmc']
        poder = dados['data'][0]['power']
        resist = dados['data'][0]['toughness']
        cor = dados['data'][0]['colors']
        mtg_url = dados['data'][0]['related_uris']['gatherer']


@app.route('/NAMEme', methods=['get', 'post'])
def nameMe():
    return 'please'


if __name__ == '__main__':
    app.run(debug=True)
