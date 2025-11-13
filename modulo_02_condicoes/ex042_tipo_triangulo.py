l1 = float(input('Medida do 1° lado: '))
l2 = float(input('Medida do 2° lado: '))
l3 = float(input('Medida do 3° lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('As retas formam triângulo', end=' ')
    if l1 == l2 == l3:
        print('\033[1;34mEquilátero')
    elif l1 != l2 != l3 != l1:
        print('\033[1;34mEscaleno')
    else:
        print('\033[1;34mIsósceles')
else:
    print('As retas não podem formar um triângulo')
