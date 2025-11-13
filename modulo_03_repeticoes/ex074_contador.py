from random import randint
n = (randint(1,10), randint(1,10),
     randint(1,10), randint(1,10),
     randint(1,10))
for t in n:
    print(f'{t} ', end='')
print(f'\nO maior valor é o {max(n)}')
print(f'O menor valor é o {min(n)}')
