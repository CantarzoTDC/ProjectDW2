import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

# colab -> https://colab.research.google.com/drive/15931qKOsZHs_BxmPCY_rU2LoSYlhJDq5?usp=sharing
# git -> https://github.com/CantarzoTDC/ProjectDW2

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['get'])
def index():  # put application's code here
    return render_template('index.html')


@app.route('/pesquisa', methods=['get'])
def getCard():
    q = request.form.get('q')
    if (q == ''):
        url = 'https://api.scryfall.com/cards/search?format=json&include_extras=false&include_multilingual=false&order=cmc&page=1&q=c%3C=wbgru&unique=cards&pretty=true'
    else:
        url = 'https://api.scryfall.com/catalog/card/search?q=' + q + '&format=json&pretty=true'

    dados = requests.get(url)

    nome = dados['data'][0]['name']
    imguri = dados['data'][0]['image_uris']['normal']
    refs = dados['data'][0]['related_uris']['gatherer']

    if dados['total_cards'] > 175:
        pages = dados['total_cards'] / 175
        nxt = dados['next_page']
        nu_page = requests.get(nxt)
    else:
        pages = 1

    return render_template('pesquisa.html', form=form)


@app.route('/NAMEme', methods=['get', 'post'])
def nameMe():
    return 'please'


if __name__ == '__main__':
    app.run(debug=True)
