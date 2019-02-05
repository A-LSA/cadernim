import  time, math
n1 = int(input('Escolha o primeiro numero: '))
n2 = int(input('Escolha o segundo numero: '))
s = 0
for n in range (n1, n2+1):
    if n % 2 == 0:
        s += n
print(s)

