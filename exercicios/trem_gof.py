

class Trem:
    def __init__(self, vagoes: int):
        self.vagoes = vagoes

    def __iter__(self):
        return IteratorTrem(self.vagoes)


class IteratorTrem:
    def __init__(self, vagoes):
        self.atual = 0
        self.ultimo_vagao = vagoes - 1

    def __next__(self):
        if self.atual <= self.ultimo_vagao:
            self.atual += 1
            return f'vagao #{self.atual}'
        else:
            raise StopIteration()


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
