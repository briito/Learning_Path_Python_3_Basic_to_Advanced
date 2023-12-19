generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator)) ERRO !!


# Versão "Normal"
# # dobro = []
# for i in range(10):
#     if i % 2 == 0:
#         dobro.append(i * 2)
# print(dobro) 