# novo salario do funcionario de 15% de aumento
salario = float(input('Qual é o salario do Funcionario? RS:'))
novo = salario + (salario *15 /100)
print('Um funcionario que ganhavaR$:{}, com aumento de 15% ele vai ganharR${}.'.format(salario,novo))