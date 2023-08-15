# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
from time import sleep
print('=' * 110)
print('-----------------------------------------PROGRESSÂO ARITIMÈTICA-----------------------------------------------')
print('='*110)
print('')
print('''        O que é uma progressão aritmética exemplos?
        Progressão arimética é uma sequência numérica em que a diferença entre um termo e seu antecessor
        resulta sempre em um mesmo valor, chamado de razão.
        Por exemplo, considere a sequência a seguir: (2, 4, 6, 8, 10, 12, 14, 16, 18, 20...)
        Podemos então dizer que a razão (r) dessa sequência numérica é 2. ''')
print('')

print('='*110)
print('-------------------------------------------10 TERMOPS DE UMA PA-----------------------------------------------')
print('='*110)

p1 = int(input('Digite O Primeiro Termo: '))
razao = int(input('Digite a Razão: '))
valor = 0
for valor in range(1, 11):
    valor = p1+razao
    sleep(0.3)
    print('{} ➔' .format(valor) )
