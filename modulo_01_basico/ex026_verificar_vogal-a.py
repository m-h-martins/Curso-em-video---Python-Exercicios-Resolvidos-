n = str(input('Digite uma frase: ')).upper().strip()
print('Quantidade de letras A: {}'.format(n.count('A')))
print('A primeira letra A, aparece na posição: {}'.format(n.upper().find('A')+1))
print('A última letra A, aparece na posição: {}'.format(n.upper().rfind('A')+1))
