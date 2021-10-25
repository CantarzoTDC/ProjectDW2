import requests, json
from flask import Flask, render_template, request, jsonify
from typing import List, Any
from rotinas import loadDados
app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/pesquisa', methods=['get'])
def getCard():
    dados:json
    q = request.form.get('search')
    if q == '':
        dados = requests.get('https://api.scryfall.com/cards/search?format=json&include_extras=false&include_multilingual=false&order=cmc&page=1&q=c%3C=wbgru&unique=cards&pretty=true').json()
    else:
        dados = requests.get('https://api.scryfall.com/catalog/card/search?q='+q).json()

    return render_template('pesquisa.html')


@app.route('/NAMEme', methods=['get', 'post'])
def nameMe():
    return 'please'


if __name__ == '__main__':
    app.run(debug=True)
