from flask import Flask, make_response, jsonify, request
from db import Titulos

app = Flask('__name__')
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def hello_world():
    return "<p> API Altos Operante!</p>"

@app.route('/titulos', methods = ['GET'])
def get_titulos():
    return make_response(
        jsonify(
            identificador='Lista de títulos.',
            titulos = Titulos)
    )

@app.route('/titulos', methods = ['POST'])
def create_titulo():
    titulo = request.json
    Titulos.append(titulo)
    return make_response(
        jsonify(
            valida='Título Cadastrado.',
            titulo=titulo)
    )


#app.run()