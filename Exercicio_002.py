# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

metros = float(input('Digite a quantidade de metros deseja converter:\n'))
centimetros = metros * 100

print('O valor digitado em metros foi {}m, sua conversão para centimetros é {:.0f}cm'.format(metros, centimetros))