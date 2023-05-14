import math
from math import hypot
#metodo com import
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adiacente: '))
hi =math.hypot(co, ca)
print('A hipotenusa vai medir {:.2}'.format(hi))

#metodo sem import
'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adiacente: '))
hi = (co ** 2 + ca ** (1/2))
print('A hipotenusa vai medir {:.2f}'.format(hi))'''