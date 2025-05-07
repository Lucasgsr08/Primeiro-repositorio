import pandas as pd 
import requests


url= "https://api.opendota.com/api/heroes"

resp = requests.get(url)   # Fazendo a requisição para a API

df = pd.DataFrame(resp.json())  # Convertendo a resposta em um DataFrame do pandas

#%%

df.to_csv("herois.csv", sep=";", index=False )  # Salvando o DataFrame em um arquivo CSV"