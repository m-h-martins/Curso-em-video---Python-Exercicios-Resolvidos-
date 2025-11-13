l = ('Pão', 1, 'Leite', 5.50, 'Picanha', 79.99,
     'Coca-Cola 2 L', 12.99, 'Arroz', 27.99)
print('='*40)
print(f'{'TABELA DE PREÇOS':^40}')
print('='*40)
for i in range(0, len(l)):
    if i % 2 == 0:
        print(f'{l[i]:.<30}', end='')
    else:
        print(f'R${l[i]:>8.2f}')
print('='*40)
