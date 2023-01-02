alunos = [('Diego', 0), ('Isabel', 10), ('Javier', 8)]


print('Utilizando o list comprehension')
print([(nome, nota) for nome, nota in alunos if nota > 5])


def possui_nota_maior_que_5(aluno):
    _, nota = aluno
    return nota > 5


print('\n Utilizando o filter')
print(list(filter(possui_nota_maior_que_5, alunos)))
