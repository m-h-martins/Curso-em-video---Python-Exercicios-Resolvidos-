print('\033[1;41m{:=^40}\033[m'.format('TABUADA'))
n = int(input('Digite um número: '))
print('='*40)
for c in range(1, 11):
    print('{}x{:2} = {}'.format(n, c, n * c))
print('='*40)
