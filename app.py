from flask import Flask
from models import detoxifyModel
from models import pySentimentModel

app = Flask(__name__);
@app.route('/')
def main():
    return "<h1>Se ha conectado Correctamente</h1>" 
@app.route('/Detoxify/Analysis/<stringInput>')
def detoxifyPredictor(stringInput):
    print("Probando Servicio...." + stringInput)
    print("IA inicializada, Probando Frase....")
    return detoxifyModel.initDetoxify()
@app.route('/PySentimiento/Analysis/<modelType>/<stringInput>')
def emotionPredictor(stringInput,modelType):
    print("Probando Servicio.... con la frase: "+ stringInput)
    return "<h3>"+pySentimentModel.sentimientoPredictor(modelType,stringInput)+"</h3>"
if __name__ == '__main__':
    app.run(debug=True, port=4000)