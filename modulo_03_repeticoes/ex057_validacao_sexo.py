s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite o seu sexo: ')).upper().strip()[0]
    if s != 'M' and s!= 'F':
        print('Resposta inválida, por favor digite novamente.')
print('Fim')
