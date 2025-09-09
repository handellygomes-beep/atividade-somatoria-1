
nome = input('qual o seu nome? ')
altura = float(input('digite aqui a sua altura: '))
peso = float(input('gigite aqui o seu peso: '))
imc = peso / (altura ** 2)
print(f'{nome} o seu imc é {imc}')
if imc <=18.5:
    print('você está abaixo do peso, procure um, expecialista que possa ajuda-lo (a)')

elif imc <= 24.9:
    print('peso normal, tudo certo')

elif imc <= 29.9:
    print('você esta com sobre peso, tome cuidado, se cuidar é importante')

elif imc <= 34.9:
    print('você está com grau de obesidade |, procure um expecialista que possa ajuda-lo (a)')

elif imc <= 39.9:
    print('você está com grau de obesidade ||, procure um expecialista que possa ajuda-lo (a)')

else:
    print('você está com o grau de obesidade |||, procure ajuda com um expecialista')