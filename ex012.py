# pegue o preço de um produto e aplique % a porcentagem de desconto nele

produto = float(input('Qual O Preço Do Produto? R$: '))
porcento = float(input('de quantos porcento é o desconto % '))


desconto = float(porcento/100)

aplicar = produto*desconto

aplicado = produto-aplicar

print(aplicado)

print('seu produto com', porcento, '% ' 'de desconto aplicado custara R${:.2f} ' .format(aplicado))
