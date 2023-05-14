from random import randint
from time import sleep
computador = randint(0,5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar em Número entre 0 e 5. \n Tente adivinhar....')

print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador adivinha
print('PROCESSANDO')
sleep(5)
if jogador == computador:
    print('PARABENS!Você conseguil me vencer!')

else:
    print('GANHEI! eu pensei no número {} e não no numero {}!'.format(computador,jogador))