l = []
while True:
    n = int(input('Digite um número: '))
    if n not in l:
        l.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não foi adicionado')
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while c not in 'SsNn':
        c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if c in 'Nn':
        break
l.sort()
print(l)
