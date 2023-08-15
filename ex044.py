# elabore um programa que calcule o valor a ser pago por um produto consioderando o seu preço normal e a condição de pagamento
# -a vista dinheiro/cheque: 10% de desconto -Avista cartão : 5% de desconto
# -em ate 2x no cartão :preço normal -3x ou mais no cartão : 20% de juros

print('-----------Lojas-Dias-----------')
preço = float(input('Qual o valor da compra: R$'))

print('Escolha a forma De Pagamento')
pay = int(input('''[1] a vista dineheiro/cheque
[2] a vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão
Qual sua opção? '''))

if pay == 1:
    calculo = 0.1*preço
    desconto = preço - calculo
    print('O valor final da conpra foi de R${:.2f}' .format(desconto))
elif pay == 2:
    calculo = 0.05*preço
    desconto = preço - calculo
    print('O valor final da conpra foi de R${:.2f}' .format(desconto))
elif pay == 3:

    print('O valor final da conpra foi de R${:.2f}' .format(preço))
elif pay ==4:
    parcelas = int(input('em quantas vezes deseja parcelar: '))
    juros = preço+(preço*20/100)
    parcela= juros/parcelas
    print('o preço das parcelas ficara em R${:.2f} em {}X vezes com juros de 20% Aplicado! Valor final: R${:.2f}' .format(
        parcela, parcelas,juros ))
else:
    print('\033[31mOPÇÂO INVALIDA!!\033[m')