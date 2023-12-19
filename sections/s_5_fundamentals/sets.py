a = {1,2,3}
# print(type(a))
a = set('coddddd3r')
# print(a)
# print(3 in a, 4 not in a)
print({1,2,3} == {3,2,1,3})

# Operações

c1 = {1,2}
c2 = {2,3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1) # Sub conjunto
print(c2 <= c1)
print(c1 >= c2) # Super conjunto
print({1,2,3} - {2})
print(c1 - c2)

# RESUMO : O conjunto é delomitado por {}, só tem valores, não é indexado, não garante ordenação e não aceita repetição.