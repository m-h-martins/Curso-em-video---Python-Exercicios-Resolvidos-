print('\033[1;44m{:=^40}\033[m'.format('Gerador de PA'))
p = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
c = 0
t = p
total = 0
b = 10
while b != 0:
    total += b
    while c < total:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    b = int(input('Você quer mostrar mais quantos termos?: '))
print('O total de termos foi de {}'.format(c))
print('FIM')
