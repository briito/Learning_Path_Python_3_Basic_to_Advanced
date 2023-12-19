# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)
# else:
#     print('Fim')    

from random import randint

def sortear_dado():
    return randint(1,6)


for n in range(1,7):
    if n % 2 == 1:
        continue

    if sortear_dado() == n:
        print('ACERTOU!!',n)
        break
    else:
        print('Não acertou o número ...')