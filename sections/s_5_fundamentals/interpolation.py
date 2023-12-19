from string import Template

# Versão mais antiga

nome, idade = 'Ana', 30
print('Nome: %s, Idade: %d' % (nome, idade)) # %s => substitui uma string /// %d => substitui um inteiro 
print('Nome: %s, Idade: %.1f' % (nome, idade)) # %f => substitui um float

#############################

print('Nome: {0} Idade: {1}'.format(nome,idade)) # python versão < 3.6

print(f'Nome: {nome} Idade {idade} {2 ** 8 + 1}')

s1 = Template('Nome: $nome Idade: $idade')
print(s1.substitute(nome=nome, idade=idade))


