# def get_tipo_dia(dia):
#     dias = {
#         1:'Fim de semana',
#         2:'Dia de semana',
#         3:'Dia de semana',
#         4:'Dia de semana',
#         5:'Dia de semana',
#         6:'Dia de semana',
#         7:'Fim de semana',
#     }
#     return dias.get(dia, 'Dia Inválido')


# for dia in range(8):
#     print(f'{dia}: {get_tipo_dia(dia)}')



########################

# A partir da versão 3.10

def get_tipo_dia(dia):
        match dia:
            case 2 | 3 | 4 | 5 | 6 :
                return 'Dia de semana'
            case 1 | 7:
                return 'Fim de semana'
            case _:
                return '** inválido **'
                
     
for dia in range(0, 9):
    print(f'{dia}: {get_tipo_dia(dia)}')