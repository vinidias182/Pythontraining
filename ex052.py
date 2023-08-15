# faça um Programa que leia um numero inteiro e diga se ele é ou não um numero primo

num = int(input(' Digite um Numero: '))
tot= 0 
print('')
for c in range (1, num + 1):
        if num % c == 0 :
            print('\033[33m', end=' ')
            tot += 1
        else:
            print('\033[31m', end=' ')
        print('{}'.format(c), end=' ')
print('')
print('\n\033[m O Numero {} foi divisivel {} vezes '.format(num,tot))
print('')
if tot == 2:
    print(' O numero É PRIMO')
else:
    print(' O Numero NÃO é PRIMO')