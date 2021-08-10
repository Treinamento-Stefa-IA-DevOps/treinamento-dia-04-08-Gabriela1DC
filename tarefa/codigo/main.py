import pickle
import pandas as pd
from fastapi import FastAPI
from sklearn import *

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

    prediction = titanic.predict([[Sex, Age, Lifeboat, Pclass]])

    if survived==True:
        return{
            'survived': prediction,
            'status': 200,
            'message': 'Sobrevivente do naufrágio do Titanic - Predição concluída!'
        }
                
    if survived==False:
        return{
            'survived': prediction,
            'status': 200,
            'message': 'Vítima do naufrágio do Titanic - Predição concluída!'
        }
    else:
        return{
            'status':500,
            'message':'Falha na execução :|'
        }

@app.get('/model')
def get():
    return {
        "Hello World"
        "Predição de sobreviventes do Titanic - API"
    }
