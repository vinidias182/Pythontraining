#nomeie 4 alunos e escolha um

from random import choice

aluno1 = input('Digite o nome: ')
aluno2 = input('Digite o nome: ')
aluno3 = input('Digite o nome: ')
aluno4 = input('Digite o nome: ')

sorteado= choice([aluno1, aluno2, aluno3 ,aluno4])

print ('o aluno sorteado foi {}' .format(sorteado))