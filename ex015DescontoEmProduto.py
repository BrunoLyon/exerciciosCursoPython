preço =float(input('Qual é o preço do produto? R$:'))
novo = preço - (preço * 5/100)
print('O produto que custava R${:2}, na promoção de 5% vai custar R$:{:2}.'.format(preço,novo))

