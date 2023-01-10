import math


class Vetor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vetor({self.x}, {self.y})'

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, vetor):
        return Vetor(self.x + vetor.x, self.y + vetor.y)

    def __iadd__(self, other):  # Não cria um novo objeto pela expressão a += b
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, n):
        return Vetor(self.x * n, self.y * n)

    def __rmul__(self, n):
        return self * n


if __name__ == '__main__':
    vetor_1 = Vetor(3, 4)
    vetor_2 = Vetor(1, 1)
    print(vetor_1)
    print(abs(vetor_1))
    print(vetor_1 + vetor_2)
    print(id(vetor_1))
    vetor_1 += vetor_2
    print(id(vetor_1))
    print(vetor_1 * 2)
