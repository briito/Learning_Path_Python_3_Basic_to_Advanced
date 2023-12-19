# Apresente o nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.

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

# Função para encontrar o(s) filme(s) mais frequente(s) e sua respectiva frequência


def find_most_frequent_movies(data):
    movie_frequency = {}  # Dicionário para armazenar a frequência de cada filme

    # Contar a frequência de cada filme
    for row in data:
        movie = row['#1 Movie']
        if movie in movie_frequency:
            movie_frequency[movie] += 1
        else:
            movie_frequency[movie] = 1

    # Encontrar a maior frequência de um filme
    max_frequency = max(movie_frequency.values())

    # Encontrar os filmes mais frequentes
    most_frequent_movies = [
        movie for movie, frequency in movie_frequency.items() if frequency == max_frequency]

    return most_frequent_movies, max_frequency


# Nome do arquivo CSV
filename = 'actors.csv'

# Ler o arquivo CSV
data = read_csv(filename)

# Encontrar o(s) filme(s) mais frequente(s) e sua respectiva frequência
most_frequent_movies, max_frequency = find_most_frequent_movies(data)

# Escrever os resultados em um arquivo task_4.txt
with open('task_4.txt', 'w') as output_file:
    output_file.write(
        f"Filme(s) mais frequente(s) e sua respectiva frequência:\n")
    for movie in most_frequent_movies:
        output_file.write(f"{movie}: {max_frequency}\n")

print("Resultado salvo em task_4.txt")
