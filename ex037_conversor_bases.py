print('\033[1;35mConversor de números\033[m')
n = int(input('Digite um número inteiro: '))
print('''Para binário, digite: \033[32m1\033[m
Para octal, digite: \033[32m2\033[m
Para hexadecimal, digite: \033[32m3\033[m''')
o = int(input('Digite a opção desejada: '))
if o == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31mOpção inválida!')
