from random import randint
n = randint(0, 10)
c = 15
t = 0
print('\033[1;44m{:=^40}\033[m'.format('JOGO DE ADIVINHAÇÃO'))
print('''Estou pensando em um número entre 0 e 10...
Em que número eu estou pensando?''')
while c != n:
    c = int(input('Digite um número: '))
    t += 1
    if n > c:
        print('Um pouco mais... Tente novamente')
    elif n < c:
        print('Menos... Tente mais uma vez')
print('Você acertou! o número que eu estava pensando era o {}'.format(n))
print('Você precisou de {} tentativas para acertar.'.format(t))
