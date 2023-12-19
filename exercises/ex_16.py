def soma_numeros_string(string_numeros):
    numeros = list(map(int, string_numeros.split(',')))
    soma = sum(numeros)

    return soma


string_numeros = "1,3,4,6,10,76"
resultado_soma = soma_numeros_string(string_numeros)
print(resultado_soma)
