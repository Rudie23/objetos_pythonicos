from random import shuffle


def funcao_geradora_naturais():
    i = 0
    while True:
        yield i
        i += 1


lista = [l for l in range(9)]
shuffle(lista)

# for i, v in enumerate(lista):
#     print(i, v)

for i, v, c in zip(funcao_geradora_naturais(), lista, 'abcde'):
    print(i, v, c)
    