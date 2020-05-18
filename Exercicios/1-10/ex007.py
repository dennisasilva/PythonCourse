# Desafio 07
# Desenvolva um programa que leia as 2 notas de um aluno, calcule e mostre a sua média

n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))
media = ((n1 + n2)/2)
print('A sua média é {}, sendo {} a 1º Nota e {} 2ª Nota'.format(media,n1,n2))
