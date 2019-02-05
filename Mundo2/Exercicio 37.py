import pyconverter

print('========================================')
print('===        Conversor numerico        ===')
print('=================V1.0===================')

escolha = input('Opa, converter para octal, binário ou hexa?'.strip())
n = 0
if escolha in ['hexa', 'hex', 'hexadecimal', '3']:
    n = int(input('Digite seu número para transformaçao: '))
    print('Seu número hexadecimal é: {} '.format(pyconverter.inttohex(n)))
elif escolha in ['octa', 'octal', 'octadecimal', '1']:
        n = int(input('Digite seu número para transformaçao: '))
        o = pyconverter.inttobin(n)
        print('Seu número hexadecimal é: {} '.format(pyconverter.bintooct(o)))
elif escolha in ['bin', 'binario', 'binary', 'binário']:
        n = int(input('Digite seu número para transformaçao: '))
        o = pyconverter.inttobin(n)
        print('Seu número hexadecimal é: {} '.format(o))
else:
        print('Escreve direito amigo!')