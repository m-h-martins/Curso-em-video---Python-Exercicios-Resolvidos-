from datetime import date
print('\033[31mCategoria dos atletas:\033[m')
n = int(input('Digite o ano de nascimento: '))
a = date.today().year
i = a - n
print('O atleta tem {} anos.'.format(i))
if i < 10:
    print('Classificação: MIRIM')
elif i < 15:
    print('Classificação: INFANTIL')
elif i < 20:
    print('Classificação: JUNIOR')
elif i < 26:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
