a = 0
e = 0
for c in range(1, 6):
    p = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        a = p
        e = p
    else:
        if p > a:
            a = p
        if p < e:
            e = p
print('O maior peso lido foi de {} Kg'.format(a))
print('O menor peso lido foi de {} Kg'.format(e))
