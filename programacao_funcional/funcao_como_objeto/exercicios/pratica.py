import operator

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
    alunos.sort(key=lambda nota: nota[1])
    alunos.sort(key=lambda aluno: aluno[0])
    return list(alunos)


print(ordenar_por_nota_e_nome_lambda(alunos))
