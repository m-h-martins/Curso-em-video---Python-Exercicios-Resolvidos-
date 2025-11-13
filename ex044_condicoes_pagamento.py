print('\033[1;36m{:=^40}\033[m'.format(' Lojas MHM '))
p = float(input('Preço do produto: R$ '))
print('\033[1;31mForma de pagamento:')
print('\033[mÀ vista dinhero/cheque, digite: \033[34m1\033[m')
print('À vista no cartão, digite: \033[34m2\033[m')
print('Até 2x no cartão, digite: \033[34m3\033[m')
print('3x ou mais no cartão, digite: \033[34m4\033[m')
f = int(input('Digite a opção desejada: '))
if f == 1:
    print('Valor final: R$ {:.2f}'.format(p*0.9))
elif f == 2:
    print('Valor final: R$ {:.2f}'.format(p*0.95))
elif f == 3:
    print('Valor final: R$ {:.2f}'.format(p))
elif f == 4:
    print('Valor final: R$ {:.2f}'.format(p*1.2))
else:
    print('\033[1;31mOpção inválida')
