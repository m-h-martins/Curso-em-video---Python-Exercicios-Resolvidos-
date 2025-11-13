cm = a = cf = 0
while True:
    print('='*30)
    print(f'\033[1;47m{'CADASTRE UMA PESSOA':^30}\033[m')
    print('='*30)
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while s != 'M' and s != 'F':
        s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('='*30)
    c = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while c != 'S' and c != 'N':
        c = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if i >= 18:
        a += 1
    if s == 'M':
        cm += 1
    if s == 'F':
        if i <= 20:
            cf += 1
    if c == 'N':
        break
print('='*30)
print(f'{a} pessoa(s) são maiores de idade')
print(f'Foram cadastrados {cm} homens')
print(f'Foram cadastradas {cf} mulheres com menos de 20 anos')
