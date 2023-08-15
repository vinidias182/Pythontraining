# analise mais complexa da frase

frase = str(input('Digite uma Frase : ')).lower().strip()

print ('A letra (A) aparece {} vezes na frase.' .format(frase.count('a')))
print ('A Primeira letra (A) aparece na posição {}'.format(frase.find('a')+1))
print ('A Ultima letra (A) aparece na posição {}'.format(frase.rfind('a')))
