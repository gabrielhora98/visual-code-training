def calcular_total(preco, quantidade):
    return preco * quantidade

print("Bem-vindo à loja!")
nome = input("Digite o seu nome: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
total = calcular_total(preco, quantidade)
print(f"O total da compra é: R$ {total:.2f}")
