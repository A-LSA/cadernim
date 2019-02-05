import math
print('========================================')
print('===    VERIFICADOR DE EMPRESTIMO     ===')
print('=================V1.0===================')

casa = int(input('Digite o valor da casa desejada: '))
salario = int(input('Digite o valor que você recebe de salário: '))
anos = int(input('Em quantos anos você pretende pagar: '))

prestacao = casa / (anos*12)
if prestacao > salario*0.30:
    print('Sentimos muito, porêm nâo podemos exceder 30% do valor do seu salário com o emprestimo.')

else:
    print('Parabéns, você conseguiu seu empréstimo consignado na KOMIO KUDIKEN TALEN DO Empréstimos')

