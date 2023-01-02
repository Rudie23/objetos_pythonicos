
"""
    Funções de alta ordem -- função que recebe outra como parâmetro
>>> def ola():
...     print('Hello')
...
>>> executar(ola)
Hello
>>> executar(ola, 2)
Hello
Hello
>>> def ola_mundo():
...     print('Hello, World')
...
>>> executar(ola_mundo, 3)
Hello, World
Hello, World
Hello, World
"""


def executar(f, n=1):
    for _ in range(n):
        f()
