from functools import wraps
from time import sleep, strftime


def logar(fn=None, *, fmt='%H:%M:%S'):  # O * indica que o parametro fmt deve ser passado de forma nomeada
    if fn is not None:  # Se você passou o parametro fmt, fn is None
        return logar(fmt=fmt)(fn)

    def decorator(f):
        @wraps(f)  # Para não ser alterada a função passada como parametro, o wraps indicará a função original
        def executar_com_tempo(*args, **kwargs):
            print(strftime(fmt))
            return f(*args, **kwargs)

        return executar_com_tempo

    return decorator


@logar  # O nome da função será modificado pela função dentro do decorator
def mochileiro():
    return 42


@logar(fmt='%d/%m/%Y %H:%M:%S')
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
