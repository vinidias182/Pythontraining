#calcule o preço da viagem convertendo a distancia em km custando 0.50 por km ate 200 km e mais que isso custando 0.45 por km

viagem =  float(input('Qual a distancia da sua viagem ? '))
valor = 0

if viagem >= 200:
    valor = viagem * 0.45
    print('A viagem custar R${:.2f}' .format(valor) )
else: 
    valor = viagem * 0.50
    print('A viagem custar R${:.2f}' .format(valor) )

    