# Crie um programa que leia a iade dos atletas e mostyre em que categoria ele se encontra
# ate 9 mirim ate 14 infantil ate 19 junior ate 25 senior acima master
from datetime import date

nasc = int(input('Informe o ano de nascimento do atleta: '))

ano = date.today().year
idade = ano-nasc

if idade <= 9:
    print('O atleta nasceui em {} e tem {} anos então ...'.format(nasc, idade))
    print('O atleta é Mirim')

elif idade <= 14:
    print('O atleta nasceui em {} e tem {} anos então ...'.format(nasc, idade))
    print('O atleta é Infantil')

elif idade <= 19:
    print('O atleta nasceui em {} e tem {} anos então ...'.format(nasc, idade))
    print('O atleta é Junior')

elif idade <= 25:
    print('O atleta nasceui em {} e tem {} anos então ...'.format(nasc, idade))
    print('o atleta é Senior')

else:
    print('O atleta nasceui em {} e tem {} anos então ...'.format(nasc, idade))
    print('O atleta é MASTER')
