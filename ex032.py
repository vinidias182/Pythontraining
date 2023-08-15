# descubra se o ano é bissexto ou não e pegue o ano do sistema 
from datetime import date

ano= int(input('Qual ano deseja analizar? Digite [0] para usar o ano atual :\033[33m'))

if ano == 0 :
# pegando data atual do sistema
    ano= date.today().year
# expressao completa para saber se é bissexto
if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 ):
    print('\033[mo ano de \033[32m{}\033[m é Bissexto' .format(ano))
else :
    print('\033[mo ano de \033[31m{}\033[m não é bissexto' .format(ano))