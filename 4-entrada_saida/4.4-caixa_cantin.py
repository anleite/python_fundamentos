#Resolução do exercicio 1
#-----Caixa Cantina-----

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade
total_br = f"{total:.2f}".replace(".",",")

print("---RESUMO DA COMPRA---")
print(f"Produto:{produto.title()} ")
print(f"Quantidade:{quantidade}")
print(f"Total a pagar: R$ {total_br}")