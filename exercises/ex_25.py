class Aviao:
    cor = "Azul"

    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade


entradas = [
    {"modelo": "BOIENG456", "velocidade_maxima": "1500 km/h",
        "capacidade": "400 passageiros"},
    {"modelo": "Embraer Praetor 600", "velocidade_maxima": "863 km/h",
        "capacidade": "14 passageiros"},
    {"modelo": "Antonov An-2", "velocidade_maxima": "258 km/h",
        "capacidade": "12 passageiros"},
]

lista_avioes = []
for entrada in entradas:
    aviao = Aviao(entrada["modelo"],
                  entrada["velocidade_maxima"], entrada["capacidade"])
    lista_avioes.append(aviao)

for aviao in lista_avioes:
    print(f"O avião de modelo \"{aviao.modelo}\" possui uma velocidade máxima de {aviao.velocidade_maxima}, "
          f"capacidade para {aviao.capacidade} e é da cor \"{aviao.cor}\".")
