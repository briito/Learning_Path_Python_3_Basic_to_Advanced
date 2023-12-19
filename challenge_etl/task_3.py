# Apresente o ator/atriz com a maior média de faturamento por filme.

# Função para ler o arquivo CSV e retornar uma lista de dicionários com os dados
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            values = line.strip().split(',')
            row = {headers[i]: values[i].strip() for i in range(len(headers))}
            data.append(row)
    return data

# Função para calcular a média de faturamento bruto por ator e encontrar o ator com a maior média


def find_actor_with_highest_average(data):
    actor_gross_total = {}  # Dicionário para armazenar o faturamento total por ator
    actor_movie_count = {}  # Dicionário para armazenar o número de filmes por ator

    # Iterar sobre os dados e calcular o faturamento total e o número de filmes por ator
    for row in data:
        actor = row['Actor']
        gross = row['Gross'].strip()

        try:
            gross = float(gross.replace(',', ''))
        except ValueError:
            continue

        if actor in actor_gross_total:
            actor_gross_total[actor] += gross
            actor_movie_count[actor] += 1
        else:
            actor_gross_total[actor] = gross
            actor_movie_count[actor] = 1

    # Encontrar o ator com a maior média de faturamento bruto por filme
    highest_average_actor = None
    highest_average = 0

    for actor, total_gross in actor_gross_total.items():
        movie_count = actor_movie_count[actor]
        average_gross = total_gross / movie_count

        if average_gross > highest_average:
            highest_average = average_gross
            highest_average_actor = actor

    return highest_average_actor, highest_average


# Nome do arquivo CSV
filename = 'actors.csv'

# Ler o arquivo CSV
data = read_csv(filename)

# Encontrar o ator com a maior média de faturamento bruto por filme
highest_average_actor, highest_average = find_actor_with_highest_average(data)

# Escrever os resultados em um arquivo task_3.txt
with open('task_3.txt', 'w') as output_file:
    output_file.write(
        f"Ator/atrizes com a maior média de faturamento por filme:\n")
    output_file.write(f"{highest_average_actor}: {highest_average:.2f}\n")

print("Resultado salvo em task_3.txt")
