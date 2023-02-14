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

dolarDF = pd.DataFrame([items_Dolar])
dolarDF = dolarDF.drop(columns=['code','codein','varBid','bid','ask', 'timestamp','pctChange'])
euroDF = pd.DataFrame([items_Euro])
euroDF = euroDF.drop(columns=['code','codein','varBid','bid','ask', 'timestamp','pctChange'])

print(dolarDF)
print(euroDF)
