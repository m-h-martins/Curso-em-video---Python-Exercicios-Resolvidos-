from emoji import emojize
from random import choice
from time import sleep
print('\033[1;46m#'*5, 'Jokenpô', '#'*5,'\033[m')
print('\033[4;31mDigite 1 para escolher: Pedra')
print('\033[4;34mDigite 2 para escolher: Papel')
print('\033[4;32mDigite 3 para escolher: Tesoura\033[m')
j = int(input('Digite a opção desejada: '))
l = [1, 2, 3]
c = choice(l)
print('='*40)
print('\033[1;46mJO\033[m')
sleep(1)
print('\033[1;46mKEN\033[m')
sleep(1)
print('\033[1;46mPÔ!\033[m')
print('='*40)
if j == 1 and c == 2:
    print('\033[1;41mEu joguei: Papel, você perdeu!\033[m', emojize('🤪'))
elif j == 1 and c == 3:
    print('\033[1;42mEu joguei: Tesoura, você venceu!\033[m', emojize('🫠'))
elif j == 2 and c == 1:
    print('\033[1;42mEu joguei: Pedra, você venceu!\033[m', emojize('🫠'))
elif j == 2 and c == 3:
    print('\033[1;41mEu joguei: Tesoura, você perdeu!\033[m', emojize('🤪'))
elif j == 3 and c == 1:
    print('\033[1;41mEu joguei: Pedra, você perdeu!\033[m', emojize('🤪'))
elif j == 3 and c == 2:
    print('\033[1;42mEu joguei: Papel, você venceu!\033[m',emojize('🫠') )
elif j == c:
    print('\033[1;47mEmpate! Jogamos a mesma coisa\033[m', emojize('🤡'))
else:
    print('\033[1;40mOpção inválida\033[m', emojize('🚫'))
