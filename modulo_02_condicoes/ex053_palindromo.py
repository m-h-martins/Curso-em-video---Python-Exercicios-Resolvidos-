f = str(input('Digite uma frase: ')).upper().strip()
l = f.split()
j = ''.join(l)
i = j[::-1]
if i == j:
    print('A frase "{}" é um palíndromo'.format(f))
else:
    print('A frase "{}" não é um palíndromo'.format(f))
