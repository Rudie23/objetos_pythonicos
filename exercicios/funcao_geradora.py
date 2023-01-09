def funcao_geradora():
    print('Inicio')
    yield 1
    yield 2
    yield 3
    print('Fim')


gerador = funcao_geradora()

for i in gerador:
    print(i)

# Não irá executar porque já consumiu a função geradora
for i in gerador:
    print(i)
print()

print("Função geradora de números naturais")


def funcao_geradora_naturais():
    i = 1
    while i <= 100:
        yield i
        i += 1


naturais = funcao_geradora_naturais()

for i in naturais:
    print(i)
