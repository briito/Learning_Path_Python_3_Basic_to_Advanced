tupla = tuple()
# tupla = ()
print(type(tupla))
print(dir(tupla))
# print(help(tupla))

tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))
print(tupla[0])

# Tuplas são imutáveis

cores = ('verde','amarelo','azul', 'azul','branco')
print(cores.index('amarelo'))
print(cores.count('azul'))
