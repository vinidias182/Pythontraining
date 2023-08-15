# escreva um programa que leia dois numeros inteiros e compare mostrando qual é maior e se sao iguais

n1 = int(input('Digite o Primeiro Valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2 :
    print('\033[32m{}\033[m é maior que \033[31m{}\033[m' .format(n1,n2))
elif n2 > n1 :
    print('\033[32m{}\033[m é maior que \033[31m{}\033[m' .format(n2,n1))
else:
    print('Os valores são iguais')
