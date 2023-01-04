from functools import wraps
from time import sleep, strftime


def logar(f):
    @wraps(f)  # Para não ser alterada a função passada como parametro, o wraps indicará a função original
    def executar_com_tempo(*args, **kwargs):
        print(strftime('%H:%M:%S'))
        return f(*args, **kwargs)

    return executar_com_tempo


@logar  # O nome da função será modificado pela função dentro do decorator
def mochileiro():
    return 42


@logar
def ola(nome):
    return f'Olá {nome}'


if __name__ == '__main__':
    print(mochileiro())
    print('Nome da função: ' + mochileiro.__name__)
    print(ola('Diego'))
    print('Nome da função: ' + ola.__name__)
    sleep(1)
    print(mochileiro())
    print(ola('Ruan'))
