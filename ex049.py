# Faça uma tabuada 2.0 usando o ciclo for

n = int(input('Digite um Numero: '))

for t in range(0, 11):
    valor = n*t
    print('\033[32m{}\033[m X \033[33m{}\033[m = \033[36m{}\033[m' .format(n, t, valor))
