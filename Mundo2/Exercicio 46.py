import  time
for fogos in range (10, 0, -1):
    if fogos == 10:
        print('Vai começar em {}'.format(fogos))
    else:
        print('               {}'.format(fogos))
    time.sleep(1)