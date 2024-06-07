import os
os.system("cls || clear")

print("\n=== Solicitando dados ===")
nome_produto = input("\nDigite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_produto = int(input("Digite a quantidade do produto: "))

if quantidade_produto <= 5:
    desconto = 0.02
elif quantidade_produto <= 10:
    desconto = 0.03
else: 
    desconto = 0.05

subtotal = preco_produto * quantidade_produto
total_pagar = subtotal - (subtotal * desconto)

print("\n=== Exibindo dados ===")
print(f"Nome do produto: {nome_produto}")
print(f"Preço do produto: {preco_produto}")
print(f"Quantidade do produto: {quantidade_produto}")
print(f"Total a pagar: {total_pagar}")

print("=== Fim ===")