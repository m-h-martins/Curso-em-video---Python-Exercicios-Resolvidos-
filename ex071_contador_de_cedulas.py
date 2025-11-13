print(f'\033[1;33m{'BANCO VEGETA':=^47}\033[m')
v = int(input('Valor a ser sacado: R$ '))
c50 = c20 = c10 = c5= c1 = 0
while True:
    if v >= 50:
        v -= 50
        c50 += 1
    else:
        if v >= 20:
            v -= 20
            c20 += 1
        else:
            if v >= 10:
                v -= 10
                c10 += 1
            else:
                if v >= 5:
                    v -= 5
                    c5 += 1
                else:
                    if v >= 1:
                        v -= 1
                        c1 += 1
                    else:
                        break
print(f'\033[1;33m{'Serão sacadas:':=^47}\033[m')
print(f'{c50} cédulas de R$ 50.00')
print(f'{c20} cédulas de R$ 20.00')
print(f'{c10} cédulas de R$ 10.00')
print(f'{c5} cédulas de R$ 5.00')
print(f'{c1} cédulas de R$ 1.00')
print('\033[1;33m=\033[m'*47)
print('Obrigado por usar o BANCO VEGETA, volte sempre!')
