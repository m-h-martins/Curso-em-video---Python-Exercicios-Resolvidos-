n = ('zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatroze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
while True:
    d = int(input('Digite um número entre 0 e 20: '))
    if 0 < d > 20:
        print('Opção inválida!')
    else:
        print(f'Você digitou o número {n[d]}')
    c = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    while c not in 'SsNn':
        c = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if c in 'Nn':
        break
