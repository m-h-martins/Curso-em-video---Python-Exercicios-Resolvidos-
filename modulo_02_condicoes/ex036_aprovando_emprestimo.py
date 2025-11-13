print('\033[1;33m='*5,'\033[1;33mSimulador de empréstimo bancário','\033[1;33m=\033[m'*5)
i = float(input('Valor do imóvel: R$ '))
s = float(input('Renda total: R$ '))
t = int(input('Quantidade de anos: '))
p = i / (t * 12)
if p <= s * 0.3:
    print('\033[1;32mSeu financiamento está aprovado!')
    print('\033[mSerão {:.0f} parcelas de R${:.2f}'.format(t*12, p))
else:
    print('\033[31mNão será possível realizar o financiamento deste imóvel.')
