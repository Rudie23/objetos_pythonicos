a = 5


# Não existe escopo global em Python
def f(a=3):
    # A preferência sempre será o escopo local
    b = 5
    print(a)
    print(globals())
    print(locals())


f()
