# Digite o salario e aplique o reajuste de 15% caso ele for menor de 1250 e 10% caso for maior

salario = float(input('Digite o valor do seu salario R$'))

if salario > 1250.00:
    aumento = salario * 0.10
if salario < 1250.00:
    aumento = salario * 0.15

reajuste = salario + aumento

print('o seu salario de \033[0;31;40m R${:.2f}\033[m  foi para \033[0;32;40m R${:.2f} \033[m' .format(salario, reajuste))
