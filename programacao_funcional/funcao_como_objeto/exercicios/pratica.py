import operator
from collections import OrderedDict

alunos = [('Javier', 10), ('Diego', 4), ('Isabel Santos', 10), ('Isabel Pereira', 10)]

print('Ordenação usando o operator')


def ordenar_por_nota_e_nome(alunos):
    alunos_ordenados_nota = sorted(alunos, key=operator.itemgetter(1))
    alunos_ordenados_nome = sorted(alunos_ordenados_nota, key=operator.itemgetter(0))
    return list(alunos_ordenados_nome)


print(ordenar_por_nota_e_nome(alunos))
print('\nMostrando as notas e alunos separadamente')
for (name, nota) in ordenar_por_nota_e_nome(alunos):
    print(f'Aluno: {name}, Nota: {nota}')

print()
print('Ordenação usando funções de alta ordem')


def ordenar_por_nota_e_nome_lambda(alunos):
    alunos.sort(key=lambda v: (v[1], v[0]))
    return list(alunos)


print(ordenar_por_nota_e_nome_lambda(alunos))

print('Order by OrderedDict()')


def ordenar_por_orderedict(alunos):
    alunos_dict = OrderedDict()
    for i in alunos:
        alunos_dict[i[1]] = i

    sorted_dict = sorted(alunos_dict.items())
    alunos_dict = [value for key, value in sorted_dict]

    return alunos_dict


print(ordenar_por_nota_e_nome_lambda(alunos))

print('Ordenação por Bubble Sort')


def ordenar_por_bubble(alunos):
    lenght = len(alunos)
    for i in range(0, lenght):
        for j in range(0, lenght - i - 1):
            if alunos[j][1] > alunos[j + 1][1]:
                tempo = alunos[j]
                alunos[j] = alunos[j + 1]
                alunos[j + 1] = tempo
    return alunos


print(ordenar_por_bubble(alunos))
