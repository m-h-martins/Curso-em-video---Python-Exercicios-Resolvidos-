n = str(input('Digite um nome: ')).strip()
x = n.split()
print('Primeiro nome: {}'.format(x[0]))
print('Último nome: {}'.format(x[len(x) - 1]))
