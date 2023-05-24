from pysentimiento import create_analyzer

def sentimientoPredictor(modelType, inputString):
    if(modelType=="STM"):
        predictor = create_analyzer(task="sentiment", lang="es")
    if(modelType=="EMT"):
        predictor = create_analyzer(task="emotion", lang="es")
    if(modelType=="HFS"):
        predictor = create_analyzer(task="hate_speech", lang="es")
    response = predictor.predict(inputString)
    return str(response)

