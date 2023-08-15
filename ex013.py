# pegue o salario do funcionario e aplique % de almento

salario = float(input('qual o salário do funcionario ? : '))

reajuste = float(input('de quantos por cento foi o reajuste ? : '))

aumento = float(reajuste/100)


novoSalario = salario + (salario*aumento)

print('seu novo salario com o reajuste de',
      reajuste, '%, sera de {}' .format(novoSalario))
