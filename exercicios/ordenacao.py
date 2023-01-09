from itertools import zip_longest

pontos = [(1, 0), (2, 1), (-1, 10), (1, -1)]

print(sorted(pontos, key=lambda v: (v[0], v[1])))

paises = ['en', 'br', 'es']

linguas = ['ingles', 'portugues', 'espanhol']

# Se quiser a maior lista, use o max()
for i in range(min(len(paises), len(linguas))):
    print(paises[i], linguas[i])

print()
lista = zip(paises, linguas)
print(list(lista))


paises = ['en', 'br', 'es', 'fr']
lista = zip(paises, linguas)
for pais, lingua in zip(paises, linguas):
    print(pais, lingua)

print()

maior_lista = list(zip_longest(paises, linguas, fillvalue='Lingua Desconhecida'))
print(maior_lista)

x = help(zip_longest)
print(x)
