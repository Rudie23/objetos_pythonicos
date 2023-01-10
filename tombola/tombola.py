from random import shuffle


class Tombola:
    def __int__(self):
        self.items = []

    def carregar(self, lista):
        self.lista = lista

    def carregada(self):
        return bool(self.items)

    def misturar(self):
        shuffle(self.items)

    def sortear(self):
        return self.items.pop()

    def __call__(self):
        return self.sortear() 
