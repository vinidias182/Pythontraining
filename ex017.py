# pegue os valores dos catetos e calcule a hipotenusa 

from math import hypot
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))

hipotenusa = hypot(co, ca)

print('a hipotenusa vai medir {:.2f}' .format(hipotenusa))
