n = int(input('Digite um numero:  '))
a = n -1
s = n +1
print('Analisando o valor {}, seu antecessor é: {} e o sucessor: {}'.format(n,a,s))

# outro modo de fazer para economizar memoria do programa
n = int(input('Digite um numero:  '))
print('Analisando o valor {}, seu antecessor é: {} e o sucessor: {}'.format(n,(n-1),(n+2)))
