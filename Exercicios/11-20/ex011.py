# Desafio 11
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua area e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma area de 2m.

alt = int(input('Digite a altura da parede em metros: '))
larg = int(input('Digite a largura da parede em metros: '))

area = alt * larg
tinta = area / 2

print('A quantidade de metros que você vai pintar é {} metros sendo necessário {:.1f} litros de tinta'.format(area,tinta))
