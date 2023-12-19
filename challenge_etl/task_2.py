# # Apresente a  média de faturamento bruto por ator.

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

# Função para calcular a média de faturamento bruto por ator


def calculate_average_gross(data):
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

    # Calcular a média de faturamento bruto por ator
    actor_average_gross = {}
    for actor, total_gross in actor_gross_total.items():
        movie_count = actor_movie_count[actor]
        average_gross = total_gross / movie_count
        actor_average_gross[actor] = average_gross

    return actor_average_gross


# Nome do arquivo CSV
filename = 'actors.csv'

# Ler o arquivo CSV
data = read_csv(filename)

# Calcular a média de faturamento bruto por ator
actor_average_gross = calculate_average_gross(data)

# Escrever os resultados em um arquivo task_2.txt
with open('task_2.txt', 'w') as output_file:
    output_file.write("Média de faturamento bruto por ator:\n")
    for actor, average_gross in actor_average_gross.items():
        output_file.write(f"{actor}: {average_gross:.2f}\n")

print("Resultado salvo em task_2.txt")
