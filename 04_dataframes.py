#%%

import pandas as pd                # importando a biblioteca pandas

#%%
idades = [                          # # criando uma lista de idades
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]
#%%
nomes = [
    'Lucas', 'João', 'Maria', 'Ana', 'Pedro',
    'Paulo', 'Rafael', 'Gustavo', 'Felipe', 'Thiago',
    'Bruno', 'Diego', 'Ricardo', 'Fernando', 'Carlos',
]
#%%
series_idades = pd.Series(idades) ## pd.Series serve para criar uma série
                                  ## serie é uma lista com índice
                                  ## indice é o número da posição do elemento na lista
                                  ## o índice começa em 0, ou seja, o primeiro elemento é o índice 0
series_nomes = pd.Series(nomes) 
#%%

df= pd.DataFrame()
df['Idade'] = series_idades
df['Nome'] = series_nomes


# %%
