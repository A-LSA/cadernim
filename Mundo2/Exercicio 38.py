print('========================================')
print('===      VERIFICADOR DE NÚMERO       ===')
print('=================V1.0===================')

n1 = float(input('Digite o 1 numero: '))
n2 = float(input('Digite o 2 numero: '))

if n1 == n2:
    print('Os dois números sao iguais')
elif n1 > n2:
    print('O primeiro numero que maior que o segundo')
else:
    print('O segundo numero é maior que o primeiro')