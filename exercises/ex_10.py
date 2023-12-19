def remover_duplicados(lista):
    conjunto_sem_duplicados = set(lista)
    lista_sem_duplicados = list(conjunto_sem_duplicados)
    return lista_sem_duplicados


lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

lista_sem_duplicados = remover_duplicados(lista_teste)
print(lista_sem_duplicados)
