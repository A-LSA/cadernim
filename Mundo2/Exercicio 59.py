import random
print('Jooj da adiviniaçao')
numero = random.randint(1,10)
print(numero)
n = 0
while n != numero:
    n = int(input('Você mesmo maconheiro que nao vai ver papai noel, qual numero eu pensei? '))
    tentativas =+ 1
print('Vose tento {}'.format(tentativas))
