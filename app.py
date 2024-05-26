import requests
import pandas as pd
import json

URL = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL'

response = requests.get( URL)

#Verifica se existe algum erro. Se existir, informa qual erro no log
response.raise_for_status()

items = json.loads(response.text)

items_Dolar = json.loads(response.text)["USDBRL"]
items_Euro = json.loads(response.text)["EURBRL"]

dropColumns = ['code','codein','varBid','bid','ask', 'timestamp','pctChange']

dolarDF = pd.DataFrame.from_dict([items_Dolar])
dolarDF = dolarDF.drop(columns=dropColumns)


euroDF = pd.DataFrame.from_dict([items_Euro])
euroDF = euroDF.drop(columns=dropColumns)

frames = [dolarDF, euroDF]

result = pd.concat(frames)

result
