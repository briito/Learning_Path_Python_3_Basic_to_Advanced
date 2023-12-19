# def nota_conceito(valor):
#     nota = float(valor)

#     if nota > 10:
#         return 'Nota Inválida'
#     elif nota >= 9.1:
#         return 'A'
#     elif nota >= 8.1:
#         return 'A-'
#     elif nota >= 7.1:
#         return 'B'
#     elif nota >= 6.1:
#         return 'B-'
#     elif nota >= 5.1:
#         return 'C'
#     elif nota >= 4.1:
#         return 'C-'
#     elif nota >= 3.1:
#         return 'D'
#     elif nota >= 2.1:
#         return 'D-'
#     elif nota >= 1.1:
#         return 'E'
#     elif nota >= 0:
#         return 'E-'
#     else:
#         return 'Nota Inválida também'


# if __name__ == '__main__':

# valor_informado = input('Digite a nota do aluno: ')
# nota_do_aluno = nota_conceito(valor_informado)
# print(nota_conceito(valor_informado))
# print('A nota do aluno foi: ',nota_do_aluno)

def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(65,100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário(a)'
    else:
        return 'Idade Inválida'
        

for idade in (17,35,83,113,-2):
    print(f'{idade}: {faixa_etaria(idade)}')











