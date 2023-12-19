ASSUNTOS_POLEMICOS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia hoje foi divertida'
]

for texto in textos:
    intersecao = ASSUNTOS_POLEMICOS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui pelo menos um palavra polêmica => ', intersecao)
    else:
        print('texto autorizado => ', texto)
