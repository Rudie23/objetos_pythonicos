"""
COnstrua uma função de ordenação que ordene os alunos por nota. Se houver empate em nota, o nome
deverá definir a ordenação.
>>> alunos = [('Diego', 4), ('Isabel Santos', 10), ('Isabel Pereira', 10), ('Javier', 10)]
>>> alunos.sort(key=ordenar_por_nota_e_nome)
>>> alunos
[('Diego', 4), ('Isabel Pereira', 10), ('Isabel Santos', 10), ('Javier', 10)]

"""
import operator


def ordenar_por_nota_e_nome(alunos):
    alunos_ordenados_nota = sorted(alunos, key=operator.itemgetter(1))
    alunos_ordenados_nome = sorted(alunos_ordenados_nota, key=operator.itemgetter(0))
    return alunos_ordenados_nome



