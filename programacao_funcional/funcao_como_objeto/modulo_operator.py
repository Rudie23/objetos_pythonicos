import operator

alunos = [('Diego', 0), ('Isabel', 10), ('Javier', 8)]

print('Utilizando o list comprehension')
print([nome for nome, nota in alunos if nota > 5])


def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5


print('\n Utilizando o map e o filter')
print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))
