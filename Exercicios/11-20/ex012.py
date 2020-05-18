# Desafio 12
# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com desconto de 5%.

prod = float(input('Digite o valor do produto: '))
desc = prod * 0.05
vfinal = prod - desc

print('O valor original do produto é {:.2f} e você tem 5% de desconto e pagará {:.2f} no produto'.format(prod, vfinal))
