class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y


x = 4
y = 5

calculadora = Calculo()
resultado_soma = calculadora.soma(x, y)
resultado_subtracao = calculadora.subtracao(x, y)

print(f"Somando: {x}+{y} = {resultado_soma}")
print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")
