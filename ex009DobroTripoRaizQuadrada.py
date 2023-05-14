#n = int(input('Digite um numero:'))
#d = n * 2
#t = n * 3
#r =n **(1/2)
#print('O dobro de {} vale {}.'.format(n,d))
#print('o tripo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f3}.'.format(n,t,n,r))

#outra forma
n = int(input('Digite um numero:'))

print('O dobro de {} vale {}.'.format(n,(n*2)))
print('o tripo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3),n, pow(n, (1/2))))