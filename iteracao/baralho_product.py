from itertools import product
from iteracao.carta import Carta


class Baralho:
    valores = [str(n) for n in range(2, 11)] + list('JQKA')
    naipes = 'paus ouros copas espadas'.split()

    def __init__(self):
        self.cartas = [Carta(v, n) for n, v in product(self.naipes, self.valores)]

    def __len__(self):
        return len(self.cartas)

    def __getitem__(self, pos):
        return self.cartas[pos]

    def __setitem__(self, pos, carta):
        self.cartas[pos] = carta


if __name__ == '__main__':
    for carta in Baralho():
        print(carta)
