# Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.

def task_1(movies):
    max_movies = max(movies, key=lambda num_qtd_movies: num_qtd_movies[2])
    return max_movies[0], max_movies[2]


def task_txt(filename, content):
    with open(filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    # Lendo o arquivo CSV e armazenando os dados em uma lista de tuplas
    with open("actors.csv", "r") as file:
        lines = file.readlines()

    # Removendo a primeira linha que contém os cabeçalhos
    lines = lines[1:]

    # Criando uma lista de tuplas para armazenar os dados
    data = [tuple(line.strip().split(",")) for line in lines]

    max_movies_actor, max_movies_count = task_1(data)
    result_text = f"Ator/atriz com maior número de filmes: {max_movies_actor} - {max_movies_count} filmes"

    task_txt("task_1.txt", result_text)
    