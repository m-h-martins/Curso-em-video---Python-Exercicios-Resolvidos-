from math import hypot
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do caceto adjacente: '))
h = hypot(o, a)
print('O comprimento da hipotenusa é: {:.2f}'.format(h))
