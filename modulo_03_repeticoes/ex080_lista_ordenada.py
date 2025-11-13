l = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > l[-1]:
        l.append(n)
        print('Adicionado ao final da lista')
    else:
        p = 0
        while p < len(l):
           if n <= l[p]:
               l.insert(p, n)
               print(f'Adicionado na {p+1}° posição da lista')
               break
           p += 1
print(f'Os valores digitados em ordem foram {l}')
