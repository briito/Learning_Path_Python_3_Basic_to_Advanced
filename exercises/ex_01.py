def ano_completara_100_anos(idade_atual):
    from datetime import datetime
    ano_atual = datetime.now().year
    ano_completara_100 = ano_atual + (100 - idade_atual)
    return ano_completara_100


def main():
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade atual: '))
    ano_centenario = ano_completara_100_anos(idade)
    print(f'{ano_centenario}\n')


main()
