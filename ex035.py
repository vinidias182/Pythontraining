# calcule 3 retas e veja se elas podem construir um triangulo

print('-='*15)
print('\033[33mAnalisador de Triangulos V1.0\033[m')
print('-='*15)

a1 = float(input('Digite o valor da 1º reta: '))
a2 = float(input('Digite o valor da 2º reta: '))
a3 = float(input('Digite o valor da 3º reta: '))

if a1 < a2 + a3 and a2 < a1+a3 and a3 < a1+a2:
    print('As Retas \033[32mPodem\033[m formar um triangulo')
else:
    print('As Retas \033[31mNão Podem\033[m formar um triangulo')
