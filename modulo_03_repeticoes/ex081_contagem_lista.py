l = []
while True:
    l.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while c not in 'SsNn':
        c = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if c in 'Nn':
        break
print(f'Foram digitados um total de {len(l)} números')
l.sort(reverse=True)
print(f'Lista em ordem decresente: {l}')
if 5 in l:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')
