import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def lerExcel():
    dataset = pd.read_csv('csv\PETR4.SA.csv')
    dataset['Date'] = pd.to_datetime(dataset['Date'])
    dataset['Variation'] = dataset['Close'].sub(dataset['Open'])

    return dataset

def Teste():
    dataset = lerExcel()
    treino = pd.DataFrame(columns = ['Open','High','Low','Volume'])

    treino['Open'] = dataset['Open']
    treino['High'] = dataset['High']
    treino['Low'] = dataset['Low']
    treino['Volume'] = dataset['Volume']

    y = dataset['Close']

    lr_model = LinearRegression()

    lr_model.fit(treino,y)

    treino['Close'] = lr_model.predict(treino)
    treino['Date'] = dataset['Date']

    return treino


    
