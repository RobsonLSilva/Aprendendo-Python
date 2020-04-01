# By Python para zumbi - Profº Fernando Masanori
# 4) Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salário: \n"))
aumento = float(input("Digite o percentual de aumento \n"))
valor_aumento = salario * aumento / 100
salario_final = salario + (salario * aumento / 100)

print("O salário base       R$ {:.2f}\nPercentual de aumento       {:.0f}%\nValor do aumento     R$  {:.2f}\nSalário final será   R$ {:.2f}".format(salario, aumento, valor_aumento, salario_final))