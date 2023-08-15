# calcular aluguel de Carros com o km valendo 0.15 e o dia 60 

usado = int(input('quantos dias ficou com o carro? : '))

rodado = float(input('quantos kms rodou com o carro? : '))

day = int(60) 

km = float(0.15)

valor = (usado * day ) + (rodado * km)

print ('voce devera pagar pelo carro o valor de {}R$' .format(valor))




