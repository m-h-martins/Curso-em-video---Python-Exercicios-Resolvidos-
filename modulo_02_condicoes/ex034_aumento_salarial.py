s = float(input('Qual é o salário do funcionário?: R$ '))
if s >= 1250:
    print('O novo salário será de: R$ {:.2f}'.format(s*1.1))
else:
    print('O noso salário será de: R$ {:.2f}'.format(s*1.15))
