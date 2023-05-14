velocidade = float(input('Qual é a velocidade do carro?  '))
if velocidade > 80:
    print('MULTA! Você excedeu o limite permitido que é de 80 Km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R$:{:.2f}'.format(multa))

else:
 print("Tenha um bom dia mantenha a velocidade")
