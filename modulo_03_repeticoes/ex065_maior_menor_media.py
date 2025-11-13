ma = me = t = q = 0
c = 'S'
while c != 'N':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    t += n
    q += 1
    if q == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    if c != 'N' and c != 'S':
        print('Opção inválida, tente novamente: ')
t = t / 2
print('Você digitou {} números e a média foi {}'.format(q, t))
print('O maior valor digitado foi o {} e o menor {}'.format(ma, me))
