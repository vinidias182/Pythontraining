# jogo de adivinhação 0.1
from random import randint
from time import sleep

print('-=-'*20)
print('Adivinhe o nume que estou pensando de 0 a 10')
print('-=-'*20)
sleep(1)

computador = randint(0,10)

jogador = int(input ('Digite um numero: '))

print('PROCESSANDO...')

sleep(1.5)
print('-=-'*20)
if jogador == computador: 
    print('VOCE ACERTOU')
else:
    print('VOCE ERROU')

print('O Numero Em Que Pensei Foi {}' .format(computador))
print('-=-'*20)