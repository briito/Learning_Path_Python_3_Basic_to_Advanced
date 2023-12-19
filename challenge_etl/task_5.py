# Apresente a lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.

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

# Função para calcular o faturamento bruto total por ator


def calculate_total_gross(data):
    actor_gross_total = {}  # Dicionário para armazenar o faturamento total por ator

    # Iterar sobre os dados e calcular o faturamento total por ator
    for row in data:
        actor = row['Actor']
        gross = row['Gross'].strip()

        try:
            gross = float(gross.replace(',', ''))
        except ValueError:
            continue

        if actor in actor_gross_total:
            actor_gross_total[actor] += gross
        else:
            actor_gross_total[actor] = gross

    return actor_gross_total


# Nome do arquivo CSV
filename = 'actors.csv'

# Ler o arquivo CSV
data = read_csv(filename)

# Calcular o faturamento bruto total por ator
actor_gross_total = calculate_total_gross(data)

# Ordenar a lista de atores pelo faturamento bruto total em ordem decrescente
sorted_actors = sorted(actor_gross_total.items(),
                       key=lambda list_total: list_total[1], reverse=True)

# Escrever os resultados em um arquivo task_5.txt
with open('task_5.txt', 'w') as output_file:
    output_file.write(
        f"Lista de atores ordenados por faturamento bruto total (em ordem decrescente):\n")
    for actor, total_gross in sorted_actors:
        output_file.write(f"{actor}: {total_gross:.2f}\n")

print("Resultado salvo em task_5.txt")
