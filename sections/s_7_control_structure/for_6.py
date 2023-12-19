ASSUNTOS_POLEMICOS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia hoje foi divertida'
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in ASSUNTOS_POLEMICOS:
            print('Texto possui pelo menos um palavra polêmica => ', palavra)
            break
    else:
        print('texto autorizado => ', texto)
