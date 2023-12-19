def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par:", numero
    else:
        return "Ímpar:", numero


def main():
    lista = []

    for i in range(3):
        num = int(input(f"Digite o {i+1}º número: "))
        lista.append(num)

    for numero in lista:
        resultado = verificar_par_impar(numero)
        print(f"{resultado[0]} {resultado[1]}")

    return lista


main()
