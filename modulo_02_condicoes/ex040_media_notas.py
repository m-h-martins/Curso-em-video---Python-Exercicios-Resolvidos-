print('\033[36mMédia do aluno\033[m')
n1 = float(input('Nota da A1: '))
n2 = float(input('Nota da A2: '))
m = (n1+n2)/2
print('A média é {:.1f}'.format(m))
if m < 5:
    print('\033[1;31mREPROVADO')
elif m >= 5 and m <= 6.9:
    print('\033[1;35mRECUPERAÇÃO')
else:
    print('\033[1;32mAPROVADO')
