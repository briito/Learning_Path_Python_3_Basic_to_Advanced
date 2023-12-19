pessoa = {
    123: 'cargo',
    'nome': 'prof.(a) Ana',
    'idade': 38,
    'cursos': ['english', 'portuguese']
}
# print(type(pessoa))
# print(pessoa)
# print(pessoa['nome'])
# print(pessoa['idade'])
# print(pessoa['cursos'][0])
# print(dir(dict))
# print(pessoa.keys())
# print(pessoa.items())
# print(pessoa.values())

pessoa['idade'] = 44
print(pessoa)
pessoa['cursos'].append('Angular')
print(pessoa)
pessoa.pop('idade')
print(pessoa)
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
