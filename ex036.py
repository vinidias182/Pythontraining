# escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. pergunrte o valor da casa, o salario
# do comprador e em quantos anos ele vai pagar. a prestçãi mensal, não pode exceder 30% do salario ou então o emprestimo sera negado

valor = float(input('Qual o valor da casa que pretende comprar: R$'))
salario = float(input('Qual o salario do comprador: R$'))
anos = int(input('Em Quantos anos o comprador pretende quitar a Casa: R$'))

print('-*-'*30)
print('\033[31m Atenção a prestação mensal não deve passar 30% do salario ou então o empréstimo sera negado\033[m')
print('-*-'*30)

ano = anos*12
mensal = valor/ano

print('O valor das parcelas em {} anos ficara em {:.2f}'.format(anos,mensal))

if mensal > 0.3*salario:
   print('O Emprestiomo foi \033[31mNEGADO\033[m')
else:
    print('O Emprestimo foi \033[32mAPROVADO\033[m')