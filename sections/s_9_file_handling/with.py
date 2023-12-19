with open('files.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
    
print('Arquivo já foi fechado !!')
