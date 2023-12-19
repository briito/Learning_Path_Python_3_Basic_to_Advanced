# Apresente o nome do ator/atriz com a maior média por filme.

import pandas as pd

df = pd.read_csv('actors.csv')

task_03 = df[df['Average per Movie'] == df['Average per Movie'].max()]

arquivo_saida = 'task_03.txt'

with open(arquivo_saida, 'w') as arquivo:
    arquivo.write(f'O ator/atriz com a maior média por filme é:\n')
    arquivo.write(f'Nome: {task_03.iloc[0]["Actor"]}\n')
    arquivo.write(
        f'Média por filme: {task_03.iloc[0]["Average per Movie"]:.2f}')
