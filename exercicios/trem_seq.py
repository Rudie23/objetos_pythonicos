# from collections import Sequence

class Trem:
    def __int__(self, num_vagoes: int):
        self.num_vagoes = num_vagoes

    def __len__(self):
        return self.num_vagoes

    def __getitem__(self, pos):
        print(pos)
        indice = pos if pos >= 0 else self.num_vagoes + pos
        if 0 <= indice < self.num_vagoes:
            return f'vagao #{indice + 1}'
        raise IndexError(f'vagao inexistente {pos}')


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
