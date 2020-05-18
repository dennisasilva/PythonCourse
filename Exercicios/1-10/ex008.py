# Desafio 08
# Escreva um programa que leia o valor em metros e exiba convertido em centímetros e milímetros

valor = float(input('Insira o valor em metros que queira converter para centímeros e milímetros: '))
cent = valor * 100
mili = valor * 1000

print('{} Metros corresponde a {:.0f} centimetros e {:.0f} milimetros'.format(valor, cent, mili))
