# Desafio 09
# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

n = int(input('Insira o número que queira transformar em tabuada: '))

for i in range(1,11):
    print('{} x {} = {}'.format(n, i, n*i))
