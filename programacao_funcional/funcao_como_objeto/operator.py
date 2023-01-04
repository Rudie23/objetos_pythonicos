import operator

lista = [(1, 2), (3, 4), (5, 6)]
pegar_primeiro = operator.itemgetter(0)
print(list(map(pegar_primeiro, lista)))
