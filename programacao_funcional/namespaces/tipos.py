a = 5


def f(a=3):
    b = 3
    print(globals())
    print(locals())
    # Ele vai buscar primeiro no escopo da função, caso não ache, ele irá no escopo global
    print(a)
    print(b)


class A:
    a = 8
    a += 1
    print(a)
    print(globals())
    print(locals())

# Cheque no python console, import this
# f()

