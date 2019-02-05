import datetime, time
print('========================================')
print('===     VERIFICADOR DE EXERCITO      ===')
print('=================V1.0===================')
anoa = str(time.strftime('%Y'))
ano = int(anoa)
anod = int(input('Qual seu ano de nascimento?'))
idade = ano - anod
if idade >= 18:
    print('Faz(em) {} ano(s) que passou sua vez de fazer o alistamento'.format(idade - 18))
elif idade == 17:
    print('Hora de se alistar coleguinha')
else:
    print('Calma lá meu patrão que falta(m) {} ano(s) pra você se alistar'.format(18 - idade))