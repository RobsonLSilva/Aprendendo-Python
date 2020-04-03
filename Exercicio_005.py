# By Python para zumbi - Profº Fernando Masanori
# 5) Solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.
preco = float(input("Digite o preço da mercadoria:\n"))
desconto = float(input("Digite o percentual de desconto:\n"))

preco_final = preco - (preco * desconto / 100)
valor_desconto = preco * desconto / 100

print("Valor a pagar     R$ {:.2f}\nValor do desconto R$ {:.2f}".format(preco_final, valor_desconto))