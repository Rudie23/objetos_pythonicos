# from collections import Sequence

class Trem:
    def __init__(self, vagoes: int):
        self.vagoes = vagoes

    def __len__(self):
        return self.vagoes

    def __getitem__(self, pos):
        print('posição na memoria:', pos)
        indice = pos if pos >= 0 else self.vagoes + pos
        if 0 <= indice < self.vagoes:
            return f'vagao #{indice + 1}'
        raise IndexError(f'vagao inexistente {pos}')


trem = Trem(4)
print(trem[0])
