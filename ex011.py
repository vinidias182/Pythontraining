# leia a altura e largura de uma parede em metros e calcule a sua área e a quantidade de tinta necessaria para pinta-la
# sabendo que cada litro de tinta pinta uma area de 2m quadrados

print("  ")
print('CONVERSOR DE ÁREA')
print("  ")
print('='*50)
largura = float(input('Digite a largura de sua parede em metros: '))
print('='*50)
altura = float(input('Digite a altura de sua parede em metros: '))
print('='*50)
print("  ")

print ('A formulá para calcular a área é : Área = L * A')

area = largura*altura
tinta = 2
m2= area/tinta
print("  ")
print('='*50)
print ('Sua Área é de : {} Metros Quadrado' .format(area))
print('='*50)


print ('Para pintar sua área considerando que um litro de tinta pinte 2 metros quadrado você precisara de: {} Litros de tinta'.format(m2))