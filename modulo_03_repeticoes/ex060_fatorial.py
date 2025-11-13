f = int(input('Digite um número: '))
c = f
t = 1
print('Calculando {}! = '.format(f), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    t *= c
    c -= 1
print('O resultado de {}! é {}'.format(f, t))
