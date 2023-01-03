
alunos = [('Diego', 0), ('Isabel', 10), ('Javier', 8)]

print('Ordenar os alunos por nota usando lamba. Use o critério de menor para maior nota')
alunos.sort(key=lambda aluno: aluno[1])
print(alunos)


def por_nome(aluno):
    return aluno[0]


print('\nOrdenar os alunos por aluno usando uma função. Em ordem crescente')
print(sorted(alunos, key=por_nome))
