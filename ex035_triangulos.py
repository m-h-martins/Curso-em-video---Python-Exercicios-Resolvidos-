l1 = float(input('Digite o comprimento de uma reta: '))
l2 = float(input('Digite o comprimento de outra reta: '))
l3 = float(input('Digite o comprimento da último reta: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
