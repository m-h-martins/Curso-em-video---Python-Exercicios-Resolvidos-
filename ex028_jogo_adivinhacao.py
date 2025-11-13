from random import randint
from time import sleep
n = randint(0,5)
print('-=-'*20)
print('Estou pensando em um número de 0 a 5...')
print('-=-'*20)
c = int(input('Em qual número eu estou pensando?: '))
print('PROCESSANDO...')
sleep(3)
if c == n:
    print('Você venceu!')
else:
    print('Você perdeu! O computador venceu! \nEu pensei no {} e não no {}'.format(n,c))
