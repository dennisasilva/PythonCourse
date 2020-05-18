#Desafio 14
#Escreva um programa que converta uma temperatura digitada em Cº e converta para Fº

c = float(input('Informe a temperatura am Cº: '))
f = ((9 * c) / 5) + 32
input('A temperatura de {}ºC corresponde a {}ºF'.format(c, f))
