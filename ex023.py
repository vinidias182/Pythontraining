# fragmente um numero e mostre suas casas decimais 

num = int(input('Transforme Um Numero: '))

u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10


print (' seu numero é {num}')
print (' seu numero tem {} unidades' .format(u))
print (' seu numero tem {} dezenas'  .format(d))
print (' seu numero tem {} centenas' .format(c))
print (' seu numero tem {} milhares' .format(m))




