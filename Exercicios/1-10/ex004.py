# Desafio 04
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre eles

text = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(text))
print('Só tem espaços? {}'.format(text.isspace()))
print('É um número? {}'.format(text.isnumeric()))
print('É alfabetico? {}'.format(text.isalnum()))
print('É alfanumérico? {}'.format(text.isalpha()))
print('Esta em maíusculas? {}'.format(text.isupper()))
print('Esta em minúsculas? {}'.format(text.islower()))
print('Está capitalizada {}'.format(text.istitle()))
