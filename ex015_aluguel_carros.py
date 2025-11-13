d = float(input('Quilometros percorridos: '))
a = int(input('Quantidade de dias do alguel: '))
dp = d * 0.15
ap = a * 60
print('Valor total a ser pago: R$ {:.2f}'.format(dp + ap))
