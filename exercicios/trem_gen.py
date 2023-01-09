
class Trem:
    def __init__(self, vagoes):
        self.vagoes = vagoes

    def __iter__(self):
        for vagao in range(1, self.vagoes + 1):
            yield f'vagao #{vagao}'


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
