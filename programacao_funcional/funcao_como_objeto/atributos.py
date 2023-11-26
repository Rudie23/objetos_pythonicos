"""
Python 3.11.1 (main, Dec 14 2022, 16:23:47) [GCC 12.2.1 20221121 (Red Hat 12.2.1-4)] on linux
Não quero investigar o retorno da função, mas os seus atributos
from programacao_funcional.funcao_como_objeto.atributos import dobro
for p in dir(dobro):
    print(p)

__annotations__
__builtins__
__call__
__class__
__closure__
__code__
__defaults__
__delattr__
__dict__
__dir__
__doc__
__eq__
__format__
__ge__
__get__
__getattribute__
__getstate__
__globals__
__gt__
__hash__
__init__
__init_subclass__
__kwdefaults__
__le__
__lt__
__module__
__name__
__ne__
__new__
__qualname__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__

> dobro.__name__
'dobro'
> dobro.__module__
'programacao_funcional.funcao_como_objeto.atributos'
> dobro.__code__.co_code
b'\x97\x00|\x00d\x01z\x05\x00\x00S\x00'

> from dis import dis
> dis(dobro.__code__.co_code)
            0 RESUME                   0
          2 LOAD_FAST                0
          4 LOAD_CONST               1
          6 BINARY_OP                5 (*)
         10 RETURN_VALUE

A funão lamba não tem o atributo __name__, pois ela não tem nome
"""


# Função é um cidadão de primeira classe
def dobro(x):
    return x * 2


dobro2 = lambda x: x * 2
