# Desafio 10
# Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
# cotação = 3,27
cot = 3.27

r = (float(input('Quanto você tem na carteira que gostaria de comprar dolar? ')))
con = r // cot
print('Você conseguirá comprar U${:.2f} doláres se tiver R${:.2f} reais'.format(con,r))
