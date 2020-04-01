# By Python para zumbi - Profº Fernando Masanori
# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

metros = float(input('Digite a quantidade de metros deseja converter:\n'))
milimetros = metros * 1000

print('O valor digitado em metros foi {}m, sua conversão para milímetros é {:.0f}mm'.format(metros, milimetros))