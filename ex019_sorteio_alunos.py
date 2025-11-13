from random import choice
print('-'*6,'Alunos que participarão do sorteio','-'*6)
a = input('Digite o nome do aluno: ')
b = input('Digite o nome de outro aluno: ')
c = input('Digite o nome de mais um aluno: ')
d = input('Digite o nome do último aluno: ')
l = [a, b, c, d]
print('O aluno escolhido é o(a) {}!'.format(choice(l)))
