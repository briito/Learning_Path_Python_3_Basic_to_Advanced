import decimal
from decimal import Decimal, getcontext

# a = 5
# b = 2.5

# print(a / b)
# print(a + b)
# print(a * b)

# print(type(a))
# print(type(b))
# print(type(a - b))

# print(b.is_integer())
# print(5.0.is_integer())
# print(int.__add__(2,3))


# print(abs(2))
# print(abs(-2))
# print(abs(- 3.5))

getcontext().prec = 2
print(Decimal(1) / Decimal(7))
# print(Decimal.max(Decimal(1), Decimal(7)))

# print(dir(Decimal))

