# TDD

Criamos e carregamos uma instância de tômbola::

```python
    >>> from tombola.tombola import Tombola
    >>> t = Tombola()

```

Após a criação, os items da tômbola são representados por uma lista vazia:

```python
    >>> t.items
    []

```

Uma lista recém criada não possui elementos. Portanto, o método "carregada" retorna falso

```python
    >>> t.carregada()
    False

```
    
É possível carregar items através do método "carregar":

```python
    >>> items = [1, 2, 3]
    >>> t.carregar(items)
    >>> t.items
    [1, 2, 3]

```

Após ser carregada, o método "carregada" retorna verdadeiro:


```python
    >>> t.carregada()
    True

```

Uma tômbola pode misturar seus items

```python
    >>> t.misturar()
    >>> items != t.items 
    False

```
