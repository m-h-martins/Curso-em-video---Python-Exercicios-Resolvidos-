import math
a = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno é: {:.2f}'.format(s))
print('O cosseno é: {:.2f}'.format(c))
print('A tangente é: {:.2f}'.format(t))
