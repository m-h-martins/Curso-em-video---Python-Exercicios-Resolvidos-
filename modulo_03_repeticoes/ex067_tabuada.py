print(f'\033[1;41m{'TABUADA':=^45}\033[m')
while True:
    n = int(input('Gostaria de ver a tabuada de que número?: '))
    if n < 0:
        break
    print('\033[1;41m=\033[m' * 45)
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c:2}')
    print('\033[1;41m=\033[m'*45)
print(f'\033[1;41m{'PROGRAMA TABUADA ENCERRADO':=^45}\033[m')
