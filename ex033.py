# programa que leia os valores e diga qual o maior e qual o menor


a = int(input('Digite um valor '))
b = int(input('Digite um segundo valor '))
c = int(input('Digite um terceiro valor '))

menor = a
maior = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c


if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

    print('o numero menor é {}' .format(menor))
    print('e o maior é {}'.format(maior))
