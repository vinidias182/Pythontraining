# identificar o primeiro e ultimo nome 

n = str(input('Digite seu nome completo : ')).strip()
nome = n.split()

print ('seu primeiro nome é : {}'.format(nome[0]))
print ('seu ultimo nome é : {}' .format(nome[len(nome)-1]))