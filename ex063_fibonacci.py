print('{:=^40}'.format('SEQUÊNCIA DE FIBONACCI'))
n = int(input('Digite um número: '))
x1 = 0
x2 = 1
c = 3
print('{} -> {}'.format(x1, x2), end='')
while c <= n:
    x3 = x1 + x2
    print(' -> {}'.format(x3), end= '')
    x1 = x2
    x2 = x3
    c += 1
print(' -> FIM')
