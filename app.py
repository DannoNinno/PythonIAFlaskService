from flask import Flask
from models import detoxifyModel
from models import pySentimentModel

app = Flask(__name__);
@app.route('/')
def main():
    return "<h1>Se ha conectado Correctamente</h1>"

@app.route('/Detoxify')
def detoxifyPredictor():

    print("Probando Servicio....")
    print("IA inicializada, Probando Frase....")
    return detoxifyModel.initDetoxify()

@app.route('/PySentimiento')
def emotionPredictor():

    print("Probando Servicio....")
    print("IA inicializada, Probando Frase....")
    return pySentimentModel.initSentimiento()

if __name__ == '__main__':

    app.run(debug=True, port=4000)