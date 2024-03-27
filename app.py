from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) # Cria uma instância do Flask. 

# Define rota da página principal
@app.route('/')
def index():
    return render_template('index.html') # Renderiza o template index.html, localizado na pasta templates

@app.route("/tabataamaral")
def infos():
 return render_template('tabataamaral.html')

@app.route("/guilhermeboulos")
def projetos():
 return render_template('guilhermeboulos.html')

@app.route("/nikolasferreira")
def publicacoes():
 return render_template('nikolasferreira.html')

if __name__ == '__main__':
  app.run(port=5000, debug=True) # Inicia o servidor na porta 5000. "Debug" é uma configuração para facilitar o desenvolvimento.
 
