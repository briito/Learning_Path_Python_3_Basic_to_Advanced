produto = {
    'nome':'Caneta azul',
    'preço': 14.99,
    'importado': True,
    'estoque': 123
}

# for chave in produto:
#     print(chave)

# for valor in produto.values():
#     print(valor)


for chave, valor in produto.items():
    print(chave, '=', valor)