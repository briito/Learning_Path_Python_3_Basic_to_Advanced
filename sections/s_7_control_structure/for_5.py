ASSUNTOS_POLEMICOS = ('futebol', 'religião', 'política')
textos = [
    'João gosta de futebol e política',
    'A praia hoje foi divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in ASSUNTOS_POLEMICOS:
            print('Texto possui pelo menos um palavra polêmica => ', palavra)
            found = True
            break

    if not found:
        print('texto autorizado => ', texto)
