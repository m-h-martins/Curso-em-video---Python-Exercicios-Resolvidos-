l = (int(input('Digite um valor: ')),
    int(input('Digite outro valor: ')),
    int(input('Digite mais um valor: ')),
    int(input('Digite o último número: ')))
print(f'O número 9 apareceu {l.count(9)} vezes')
if 3 in l:
    print(f'O valor 3 aparece pela primeira vez no {l.index(3)+1}° valor')
else:
    print(f'O valor de 3 não foi digitado nenhuma vez')
print('Os valores pares digitados foram: ', end='')
for c in l:
    if c % 2 == 0:
        print(c, end=' ')
