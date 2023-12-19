# Apresente a média da coluna contendo o número de filmes.

import pandas as pd

df = pd.read_csv('actors.csv')

task_02 = df['Number of Movies'].mean()

arquivo_saida = 'task_02.txt'

with open(arquivo_saida, 'w') as arquivo:
    arquivo.write(f'A média do número de filmes é: {task_02:.2f}')
