# um programa que jogue pedra pappel e tesoura com o usuario
from time import sleep
from random import randint

print('''Suas Opçoes:
      [1]PEDDRA
      [2]PAPEL
      [3]TESOURA''')

jogada = int(input('Qual sua jogada? '))

jogadapc = randint(1, 3)

print('')
sleep(0.5)
print('         --JO--')
sleep(0.5)
print('         --KEN--')
sleep(0.5)
print('         --PO!!--')

print('')

print('Computador:{}'.format(jogadapc))

if jogada == 1 and jogadapc == 1:
    print('EMPATE')
    dnv = int(input('Jogar novamente [1] para sim e [2] para não: '))

    if dnv == 1:
        for c in range(jogadapc):
          c
    else:
     print('Fim')
elif jogada == 1 and jogadapc == 2:
    print('Voce perdeu')
elif jogada == 1 and jogadapc == 3:
    print('Voce Venceu!!')
elif jogada == 2 and jogadapc == 1:
    print('Voce Venceu!!')
elif jogada == 2 and jogadapc == 2:
    print('EMPATE')
elif jogada == 2 and jogadapc == 3:
    print('Voce Perdeu')
elif jogada == 3 and jogadapc == 1:
    print('Voce Perdeu')
elif jogada == 3 and jogadapc == 2:
    print('Voce Venceu!!')
elif jogada == 3 and jogadapc == 3:
    print('EMPATE')

else:
    print('JOGADA INVALIDA')
