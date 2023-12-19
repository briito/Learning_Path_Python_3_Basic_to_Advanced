def my_map(lista, function):
    resultados = []
    for elemento in lista:
        resultado = function(elemento)
        resultados.append(resultado)

    return resultados


def quadrado(numero):
    return numero ** 2


lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado_final = my_map(lista_entrada, quadrado)
print(resultado_final)
