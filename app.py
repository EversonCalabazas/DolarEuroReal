import requests
import pandas as pd
import json
import smtplib
import email.message
from IPython.display import HTML

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

dolar = dolarDF.to_html()
euro = euroDF.to_html()

from email.policy import SMTP
import smtplib
import email.message

corpo_email = f"""
<p>Olá Everson</p>
<p>Email automático</p>
"{dolar}"
"{euro}"
"""

msg = email.message.Message()
msg['Subject'] = "Assunto"
msg['From'] = "everson.esc@gmail.com"
msg['To'] = "everson.esc@gmail.com"
password = 'ezhhrsdurruzrvlo'
msg.add_header('Content-Type','text/html')
msg.set_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()

s.login(msg['From'], password)
s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
print('Email enviado')
