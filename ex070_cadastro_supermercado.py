print('-'*50)
print(f'\033[1;33m{'PRÍNCIPE DOS SAIYAJINS ATACADISTA':^50}\033[m')
print('-'*50)
t = c = caro = vcaro = 0
pcaro = ''
while True:
    p = str(input('Nome do produto: ')).strip()
    v = float(input('Preço do produto: R$ '))
    t += v
    caro += 1
    if v > 1000:
        c += 1
    if caro == 1 or v > vcaro:
        pcaro = p
        vcaro = v
    s = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while s != 'S' and s != 'N':
        s = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if s == 'N':
        break
print('-'*50)
print(f'O total da compra é R$ {t:.2f}')
print(f'{c} Produtos que custam mais de R$ 1000.00')
print(f'O produto mais caro é o {pcaro}')
