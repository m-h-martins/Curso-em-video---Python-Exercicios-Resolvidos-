print('\033[1;44m{:=^40}\033[m'.format('Gerador de PA'))
p = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 0
t = p
while c < 10:
    print('{}'.format(t), end='')
    print(' -> ' if c < 9 else '', end='')
    t += r
    c += 1
