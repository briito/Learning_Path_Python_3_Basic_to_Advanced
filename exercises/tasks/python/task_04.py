# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

import pandas as pd

df = pd.read_csv('actors.csv')

task_04 = df['#1 Movie'].mode()
frequencia = df['#1 Movie'].value_counts().max()

arquivo_saida = 'task_04.txt'

with open(arquivo_saida, 'w') as arquivo:
    arquivo.write(f'Os filmes mais frequentes são:\n')
    for filme in task_04:
        arquivo.write(f'Nome do Filme: {filme}\n')
    arquivo.write(f'Frequência: {frequencia}')
