from random import randint
from time import sleep
print(f'\033[4;36m{'PAR OU ÍMPAR':^53}\033[m')
cont = 0
while True:
    e = str(input('Escolha [P] para PAR ou [I] para ÍMPAR: ')).strip().upper()[0]
    while e not in 'PI':
        e = str(input('Escolha [P] para PAR ou [I] para ÍMPAR: ')).strip().upper()[0]
    p = int(input('Digite o valor que irá jogar: '))
    c = randint(0,10)
    print(f'Eu jogo {c}')
    sleep(1)
    r = (p + c) % 2
    if r == 0:
        r = 'P'
    else:
        r = 'I'
    if r != e:
        break
    else:
        print('\033[1;42mVocê Venceu!\033[m')
        print('-' * 53)
        cont += 1
print('-'*53)
print(f'\033[4;36mVocê venceu {cont} vezes consecutivas!\033[m')
print('\033[1;41mGAMEOVER\033[m')
