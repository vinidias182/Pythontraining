#Multa de carro se ultrapassar 80km

from time import sleep
velocidade =  float(input('Qual a velocidade do carro : '))

if velocidade > 80 :
    multa = (velocidade-80)*(7)
    print('Limite ultrapassado de 80Km/h')
    print('CALCULANDO MULTA...')
    sleep(1)
    print('Voce foi multado Deve pagar {:.2f}R$' .format(multa))
else: 
    print (' Tenha um Bom Dia Dirija com Segurança ')

