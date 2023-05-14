
nome = str(input('Qual é seu nome ?'))
# se eu por sinal > alinhamento a direita
print('prazer em te conhecer {:>20}!'.format(nome))

nome = str(input('Qual é seu nome ?'))
#se eu por sinal < alinhamento a esquerda
print('prazer em te conhecer {:<20}!'.format(nome))

#se eu por sinal ^ centralizado
nome = str(input('Qual é seu nome ?'))
#se eu por sinal ^ centralizado
print('prazer em te conhecer {:^20}!'.format(nome))

nome = str(input('Qual é seu nome ?'))
#se eu por um sinal por exemplo esse = ele prenche os espacos vazios com ele
print('prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor:  '))
n2 = int(input('Outro valor:  '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, \n o produto é {},\n e a divisão é {}'.format(s,m,d))
print ('Divisão inteira é {}, \n a potencia é {}'.format(di, e))

