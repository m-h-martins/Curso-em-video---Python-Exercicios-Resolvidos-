# Soma dos números pares
s = 0
y = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        s += n
        y += 1
print('Você digitou {} números pares e a somatória é igual a {}'.format(y, s))
