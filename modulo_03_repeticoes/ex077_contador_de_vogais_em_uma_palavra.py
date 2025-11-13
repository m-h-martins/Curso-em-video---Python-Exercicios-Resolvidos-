t = ('Vegeta', 'Frango', 'Corinthians', 'Depay', 'Sukuna', 'Preto', 'Murilo')
for c in t:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for p in c:
        if p.lower() in 'aeiou':
             print(p, end=' ')
