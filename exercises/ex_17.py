def dividir_em_tres_partes(lista):
    tamanho_parte = len(lista) // 3
    if len(lista) % 3 != 0:
        return None

    parte1 = lista[:tamanho_parte]
    parte2 = lista[tamanho_parte: 2 * tamanho_parte]
    parte3 = lista[2 * tamanho_parte:]

    return parte1, parte2, parte3


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_em_tres_partes(lista)

print(parte1, parte2, parte3)
