def is_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def imprimir_primos():
    primos = []
    for numero in range(1, 101):
        if is_primo(numero):
            primos.append(numero)
    return primos


primos = imprimir_primos()
for primo in primos:
    print(primo)
