# analise o texto 

nome = input('Digite seu Nome Completo: ')

maiuscula = nome.upper()
minuscula = nome.lower()
tamanho = len(nome)
firstName = nome.split()[0]
formatando = nome.title()


print ('Analisando o nome {}' .format(nome))
print ('seu nome formatado fica {}' .format(formatando))
print ('Seu nome em Maiusculo fica {}' .format(maiuscula))
print ('Seu nome em Minusculo fica {}' .format(minuscula))
print ('seu nome possui {} letras' .format(tamanho))
print ('e seu primeiro nome é {} e possui {} letras '. format(firstName, len(firstName)))
