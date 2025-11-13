from random import shuffle
print('='*5, 'Ordem de apresentação', '='*5)
a1 = input('Nome do 1° aluno: ')
a2 = input('Nome do 2° aluno: ')
a3 = input('Nome do 3° aluno: ')
a4 = input('Nome do 4° aluno: ')
o = [a1, a2, a3, a4]
shuffle(o)
print('A ordem de apresentação é:')
print(o)