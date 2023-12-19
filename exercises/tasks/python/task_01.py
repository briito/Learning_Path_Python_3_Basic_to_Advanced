# Identifique o ator/atriz com maior número de filmes e o respectivo número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

task_01 = df[df['Number of Movies'] == df['Number of Movies'].max()]

arquivo_saida = 'task_01.txt'

with open(arquivo_saida, 'w') as arquivo:
    arquivo.write(f'O ator/atriz com o maior número de filmes é:\n')
    arquivo.write(f'Nome: {task_01.iloc[0]["Actor"]}\n')
    arquivo.write(f'Número de filmes: {task_01.iloc[0]["Number of Movies"]}')
