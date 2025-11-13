from datetime import date
h = date.today().year
tm = 0
te = 0
for c in range(1, 8):
    a = int(input('Ano de nascimento da {} pessoa: '.format(c)))
    d = h - a
    if d >= 18:
        tm += 1
    else:
        te += 1
print('Tivemos {} pessoas maiores de idade.'.format(tm), end=' ')
print('E tivemos {} pessoas menores de idade'.format(te))
