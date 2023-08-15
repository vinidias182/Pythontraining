# exercicio 004 digite um numero e mostre as especificaçoes dele 

n = input('digite algo: ')
print(n, 'é de que tipo :', type(n))
print(n, 'é numerico :', n.isnumeric())
print(n, 'é string :', n.isalpha())
print(n, 'é alphanumerico :', n.isalnum())
 