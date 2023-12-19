primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for indice, idade in enumerate(idades):
    primeiroNome = primeirosNomes[indice]
    sobreNome = sobreNomes[indice]

    print(f"{indice} - {primeiroNome} {sobreNome} está com {idade} anos")
