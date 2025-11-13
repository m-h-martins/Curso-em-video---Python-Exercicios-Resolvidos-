o = 0
m = 0
while o != 5:
    v1 = int(input('Digite um número: '))
    v2 = int(input('Digite outro número: '))
    print('''O que você deseja fazer com esses valores? 
[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números\n[5] Sair do programa''')
    o = int(input('Digite a opção desejada: '))
    if o == 1:
        print('A soma de {} e {} é igual a {}'.format(v1, v2, v1 + v2))
    elif o == 2:
        print('Multiplicando {} com {} temos {}'.format(v1, v2, v1 * v2))
    elif o == 3:
        m = v1
        if m < v2:
            m = v2
        print('O maior valor entre {} e {} é {}'.format(v1, v2, m))
        if v1 == v2:
            print('Os valores são iguais!!!')
    elif o == 4:
        print('Retornando ao início...')
    elif o == 5:
        ''
    else:
        print('Opção inválida, tente novamente')
    print('='*45)
print('Fim')
