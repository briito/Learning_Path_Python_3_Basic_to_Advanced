# Listas de entrada
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

set_lista_a = set(a)
set_lista_b = set(b)
intersecao = set_lista_a & set_lista_b
lista_intersecao = list(intersecao)
print(lista_intersecao)
