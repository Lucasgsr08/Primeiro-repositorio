
import requests     # Importando a biblioteca requests para fazer requisições HTTP
import json         # para tratar listas e dicionários para json
from tqdm import tqdm  # Importando tqdm para mostrar a barra de progresso


ceps = [
    "01001-000",  # Praça da Sé - SP
    "30130-010",  # Belo Horizonte - MG
    "20040-010",  # Rio de Janeiro - RJ
    "70040-010",  # Brasília - DF
    "80010-000",  # Curitiba - PR
    "40020-000"   # Salvador - BA
    "74820-110"   # Goiânia - GO
    "70040-010"   # Brasília - DF
    
]

url = "https://viacep.com.br/ws/{ceps}/json/"
dados = []
for i in tqdm(ceps):    
    resposta = requests.get(url.format(ceps=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados 

print(dados)

with open ("cep.json", "w", encoding ='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)
#%%
