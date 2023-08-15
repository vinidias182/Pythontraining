# Escreva um programa que converta um numero inteiro para as bases de converção escolhida
n = int(input('DIGITE UM NUMERO INTEIRO: '))

print('''escolha uma opção para converter seu numero:
[1] BINáRIO
[2] OCTAL
[3] HEXADECIMAL''')

opção = int(input('DIGITE SUA OPÇAO: '))

if opção == 1:
    print('{} Convertido para binario fica \033[1;7;32;40m{}\033[m' .format(n, bin(n) [2:]))
elif opção == 2:
    print('{} Convertido para octal Fica \033[1;7;32;40m{}\033[m' .format(n,oct(n)[2:]))
elif opção == 3:
    print('{} Convertido para hexadecimal Fica \033[1;7;32;40m{}\033[m' .format(n,hex(n)[2:]))
else:
    print('\033[31mOpcão invalida')