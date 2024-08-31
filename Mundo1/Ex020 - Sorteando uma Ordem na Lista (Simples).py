from random import shuffle

alunos = []

for i in range(4):
    aluno = str(input(f'Qual o nome do {i + 1}° aluno: '))
    alunos.append(aluno)

# SHUFFLE = significa embaralhar
shuffle(alunos)
print(f'A ordem de apresentação será:\n{alunos}')