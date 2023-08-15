#nomeie 4 alunos e os distribua em ordem aleatoria

from random import shuffle

aluno1 = str(input('Digite o nome: '))
aluno2 = str(input('Digite o nome: '))
aluno3 = str(input('Digite o nome: '))
aluno4 = str(input('Digite o nome: '))

list = [aluno1, aluno2, aluno3, aluno4]

shuffle(list)

print('a orde de alunos sorteados foi {}' .format(list))
