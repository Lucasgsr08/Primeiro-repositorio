import requests  # type: ignore
import json
from tqdm import tqdm  # cria uma barra de progresso no terminal//para medir progresso
ceps = [
    "01001-000",  # Praça da Sé - SP
    "30130-010",  # Belo Horizonte - MG
    "20040-010",  # Rio de Janeiro - RJ
    "70040-010",  # Brasília - DF
    "80010-000",  # Curitiba - PR
    "40020-000"   # Salvador - BA
]



url = "https://viacep.com.br/ws/{cep}/json/"
dados = []

for cep in tqdm(ceps):
    cep_limpo = cep.strip()
    resposta = requests.get(url.format(cep=cep_limpo))
    if resposta.status_code == 200:
        dados.append(resposta.json())


# Exibe um resumo no terminal
print(f"{len(dados)} CEPs encontrados com sucesso.")

# Salva os dados no arquivo JSON
with open("ceps.json", "w", encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)
