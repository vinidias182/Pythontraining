# faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele ainda vai se alistar
# ao serviço militar; se é hora de alistar ou se ja passou o tempo para se alistar.
from datetime import date

nasc = int(input('Informe qual seu ano de nascimento?: '))
ano= date.today().year
idade = ano-nasc
nescessario = 17
calcular= nescessario - idade
proximadata= ano+calcular


if idade == 17 :
    print('Voce ja possui {} esta na idade de se alistar em {}'.format(idade,ano))

elif idade<17:
    print('Voce nasceu em {} e possui {} anos seu alistamento sera no ano de {}' .format(nasc,idade,proximadata))

else:
    print('Voce possui {} anos, deveria ter se alistado ' .format(idade))