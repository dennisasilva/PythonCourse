# Desafio 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

sal = float(input('Digite o valor do seu salário: '))
aumento = sal + (sal * 0.15)

print('O seu novo salário é {:.2f} e você teve um aumento de 15%'.format(aumento))
