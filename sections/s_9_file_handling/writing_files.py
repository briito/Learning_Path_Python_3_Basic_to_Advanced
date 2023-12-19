with open('files.csv') as arquivo:
    with open('files.txt','w') as saída:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saída)
    
print('Arquivo já foi fechado !!')
