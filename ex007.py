# receba duas notas e calcule a media do aluno com if e else dependendo da media

import math

m = ('Média do aluno')

print('{:=^50}' .format(m))

nome = input('Digite seu nome: ')

n1 = float(input('{} nos informe sua primeira nota: ' .format(nome)))
n2 = float(input('{} nos informe sua segunda nota: ' .format(nome)))

media = math.ceil(n1+n2) / 2

print(nome, 'a sua média foi de: {} ' .format(media))

if media >= 5.0:
    print('parabéns você passou')

else:
    print('você reprovou')
