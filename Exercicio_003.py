# By Python para zumbi - Profº Fernando Masanori
# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
# Cada dia tem 24 horas ou 1440 minutos ou 86.400 segundos
# Cada hora tem 60 minutos ou 3.600 segundos
# Cada minuto tem 60 segundos
# Segundos digitados seram apenas somados

print("============================")
print("Conversor para segundos!!!")
print("============================\n")

dias = int(input("Digite a quantidade de dias: \n"))
horas = int(input("Digite a quantidade de horas: \n"))
minutos = int(input("Digite a quantidade de minutos: \n"))
segundos = int(input("Digite a quantidade de segundos: \n"))

total_segundos = (dias * 24 * 3600) + (horas * 60 * 60) + (minutos * 60) + segundos

print("O valor total em segundos é de {}s.".format(total_segundos))


