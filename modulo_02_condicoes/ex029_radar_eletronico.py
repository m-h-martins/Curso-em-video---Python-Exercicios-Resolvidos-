v = int(input('Velocidade do carro em km/h: '))
if v>80:
    print('O carro foi multado!')
    print('O valor da multa é de: R$ {:.2f}'.format((v-80)*7))
else:
    print('Veículo dentro do limite de velocidade!')
