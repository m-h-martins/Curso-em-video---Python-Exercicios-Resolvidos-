l = []
#maior = 0
#menor = 0
for v in range(0, 5):
    l.append(int(input(f'Digite um número para a posição {v}°: ')))
    #if c == 0:
        #maior = menor = l[v]
    #else:
        #if l[v] > maior:
            #maior = l[v]
        #if l[v] < menor:
            #menor = l[v]
print('='*60)
print(f'Você digitou os valores {l}')
print(f'O maior valor digitado foi {max(l)}, nas posições: ', end= '')
for p, c in enumerate(l):
    if c == max(l):
        print(f'{p}°...', end= ' ')
print(f'\nO menor valor digitado foi {min(l)}, nas posições: ', end= '')
for p , c in enumerate(l):
    if c == min(l):
        print(f'{p}°...', end= ' ')
