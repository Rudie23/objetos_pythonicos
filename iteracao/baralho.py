
class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return f'Carta(valor={self.valor}, naipe={self.naipe})'


class Baralho:
    valores = [str(n) for n in range(2, 11)] + list('JQKA')
    naipes = 'paus ouros copas espadas'.split()

    def __init__(self):
        self.cartas = [Carta(valor, naipe) for naipe in self.naipes for valor in self.valores]

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __setitem__(self, pos, carta):
        self.cartas[pos] = carta


if __name__ == '__main__':
    for carta in Baralho():
        print(carta)
