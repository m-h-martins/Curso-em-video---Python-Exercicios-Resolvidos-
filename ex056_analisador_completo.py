m = 0
h = 'm'.upper()
f = 'f'.upper()
ft = 0
ht = 0
v = 0
for p in range(1, 5):
    print('='*10,'{}° Pessoa'.format(p),'='*10)
    n = str(input('Nome: ')).strip().upper()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    m += i
    if s == h:
        if p == 1:
            ht = i
            v = n.capitalize()
        if ht < i:
            ht = i
            v = n.capitalize()
    if s == f:
        if i < 20:
            ft += 1
print('A média de idade do grupo é {:.1f} anos'.format(m/4))
print('O homem mais velho é o {} e ele tem {} anos'.format(v, ht))
print('E {} mulher(es) tem menos de 20 anos'.format(ft))
