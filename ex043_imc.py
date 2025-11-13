print('-=-'*3, '\033[4;33mCálculo do IMC\033[m', '-=-'*3)
p = float(input('Digite o peso em quilos: '))
a = float(input('Digite a altura em metros: '))
imc = p / a ** 2
if imc < 18.5:
    print('IMC = {:.2f}\nStatus: \033[1;36mAbaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC = {:.2f}\nStatus: \033[1;32mPeso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC = {:.2f}\nStatus: \033[1;33mSobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC = {:.2f}\nStatus: \033[1;31mObesidade'.format(imc))
else:
    print('IMC = {:.2f}\nStatus: \033[1;31mObsediade mórbida'.format(imc))
