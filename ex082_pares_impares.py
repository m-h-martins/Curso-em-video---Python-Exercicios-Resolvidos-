l0 = []
l1 = []
l2 = []
while True:
    n = l0.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while c not in 'SsNn':
        c = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if c in 'Nn':
        break
for p, c in enumerate(l0):
    if c % 2 == 0:
        l2.append(c)
    else:
        l1.append(c)
print(f'Números digitados: {l0}')
print(f'Números ímpares: {l1}')
print(f'Números pares: {l2}')
