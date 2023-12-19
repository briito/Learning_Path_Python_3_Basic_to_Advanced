# def get_dia_semana(dia):
#     dias = {
#         1:'Domingo',
#         2:'Segunda',
#         3:'Terça',
#         4:'Quarta',
#         5:'Quinta',
#         6:'Sexta',
#         7:'Sábado',
#     }
#     return dias.get(dia, 'Dia Inválido')

# for dia in range(0,9):
#     print(f'{dia}: {get_dia_semana(dia)}')

########################

# A partir da versão 3.10

def get_dia_semana(dia):
    match dia:
        case 1:
            return 'Domingo'
        case 2:
            return 'Segunda'
        case 3:
            return 'Terça'
        case 4:
            return 'Quarta'
        case 5:
            return 'Quinta'
        case 6:
            return 'Sexta'
        case 7:
            return 'Sabado'
        case _:
            return '** inválido **'


for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')