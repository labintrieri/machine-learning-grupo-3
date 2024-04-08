#arrumar boulos e zambelli
#melhorar engenharia de prompt
#arrumar parte dos app route que tem que escrever o nome_deputado, deveria ser variável
#centralizar html 
#colocar tokens em variáveis
#colocar resto do código em outro arquivo py? a ver

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) # Cria uma instância do Flask. 
from pymongo import MongoClient
import os

mongodb_uri = os.getenv('MONGO_URI')
db_name = os.getenv('MONGO_ID')

# Inicia a conexão com o MongoDB
client = MongoClient(mongodb_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client[db_name]  # Usa o nome do banco de dados correto

# Define rota da página principal
@app.route('/')
def index():
    return render_template('index.html') # Renderiza o template index.html, localizado na pasta templates

@app.route("/tabataamaral")
def tabataamaral():
    documentos = list(db.resumos_deputados.find({"nome_deputado": "Tabata Amaral"}))
    if documentos:
        return render_template('tabataamaral.html', documentos=documentos)
    else:
        return "Informações da deputada Tabata Amaral não encontradas", 404

@app.route("/guilhermeboulos")
def guilhermeboulos():
    documentos = list(db.resumos_deputados.find({"nome_deputado": "Boulos"}))
    if documentos:
        return render_template('guilhermeboulos.html', documentos=documentos)
    else:
        return "Informações do deputado Guilherme Boulos não encontradas", 404

@app.route("/nikolasferreira")
def nikolasferreira():
    documentos = list(db.resumos_deputados.find({"nome_deputado": "Nikolas Ferreira"}))
    if documentos:
        return render_template('nikolasferreira.html', documentos=documentos)
    else:
        return "Informações do deputado Nikolas Ferreira não encontradas", 404

@app.route("/carlazambelli")
def carlazambelli():
    documentos = list(db.resumos_deputados.find({"nome_deputado": "Zambelli"}))
    if documentos:
        return render_template('carlazambelli.html', documentos=documentos)
    else:
        return "Informações da deputada Carla Zambelli não encontradas", 404

@app.route("/eduardobolsonaro")
def eduardobolsonaro():
    documentos = list(db.resumos_deputados.find({"nome_deputado": "Eduardo Bolsonaro"}))
    if documentos:
        return render_template('eduardobolsonaro.html', documentos=documentos)
    else:
        return "Informações do deputado Eduardo Bolsonaro não encontradas", 404

@app.route("/ricardosalles")
def ricardosalles():
    documentos = list(db.resumos_deputados.find({"nome_deputado": "Ricardo Salles"}))
    if documentos:
        return render_template('ricardosalles.html', documentos=documentos)
    else:
        return "Informações do deputado Ricardo Salles não encontradas", 404

if __name__ == '__main__':
  app.run(port=5000, debug=True) # Inicia o servidor na porta 5000. "Debug" é uma configuração para facilitar o desenvolvimento.
 
