from datetime import date
print('\033[32mPrograma de alistamento militar\033[m')
a = int(input('Digite o ano de nascimento: '))
h = date.today().year
i = h - a
d = i - 18
v = 18 - i
print('Você nasceu em {} e tem {}'.format(a, i))
if i > 18:
    print('''Você já deveria ter se alistado há {} anos.
O seu ano de alistamento foi em {}.'''.format(d, h- d))
elif i < 18:
    print('''Ainda faltam {} anos.
Seu alistamento será em {}.'''.format(v, h + v ))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')
