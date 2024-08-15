set_inicial = {11, 12, 13, 14}
print(set_inicial)

set_inicial.add(15)
print(set_inicial)

set_inicial.update({1, 2, 3, 4, 5})
print(set_inicial)

set_inicial.discard(13)
print(set_inicial)

novo_set = set([20, 21, 23, 1, 2])
print(novo_set)

uniao = set_inicial.union(novo_set)
print(uniao)

interseccao = set_inicial.intersection(novo_set)
print(interseccao)

diferenca = set_inicial.difference(novo_set)
print(diferenca)

diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print(diferenca_simetrica)
