# calcule as retas e diga se ela pode virar um triangulo e se sim qual tipo de triangulo ela sera
# escaleno = todos lados iguais , isoceles: dois lados iguais

a1 = float(input('Digite o valor da 1º reta: '))
a2 = float(input('Digite o valor da 2º reta: '))
a3 = float(input('Digite o valor da 3º reta: '))
equilatero = (a1+a2+a3) / 3


if a1 < a2 + a3 and a2 < a1+a3 and a3 < a1+a2:
    print('As Retas \033[32mPodem\033[m formar um triangulo')
    
else:
    print('As Retas \033[31mNão Podem\033[m formar um triangulo')


if equilatero == a1 and equilatero == a2 and equilatero == a3:
    print('Equilatero')

elif a1 != a2 and a1 != a3 and a3 != a1 and a2 != a3 :
    print('Escaleno')

else:
    print('isóceles')