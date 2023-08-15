# calcule o indice de imc do paciente

peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite sua altura em M: '))
imc = (peso/(altura**2))

print('O seu Valor de IMC é de : {} e voce se encontra em estado de ...'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobre peso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
 