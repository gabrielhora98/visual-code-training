produtos = [ 
            {"categoria": "camisa",
            "nome": "camisa 1 oficial", 
            "preço": "R$ 299,90", 
            "quantidade": 10, 
            "tamanho": "M"},

            {"categoria": "calça",
                "nome": "calça 1 oficial", 
                "preço": "R$ 399,90", 
                "quantidade": 5, 
                "tamanho": "M"},

                {"categoria": "Casaco",
                "nome": "casaco viagem 1 oficial", 
                "preço": "R$ 599,90", 
                "quantidade": 8, 
                "tamanho": "G"} ]

nome_procurado = input("Digite o nome do produto que deseja buscar: ").lower()
encontrado = False
quantidade_encontrada = 0 
for produto in produtos:
    if nome_procurado in produto["nome"].lower():
            print(f"Produto encontrado: {produto['nome']}")
            print(f"preço: {produto['preço']}")
            print(f"quantidade: {produto['quantidade']}")
            print(f"tamanho: {produto['tamanho']}")
            encontrado = True
            quantidade_encontrada += 1


if encontrado == False:
    print("Produto não encontrado.")
else:
    print(f"Quantidade total encontrada: {quantidade_encontrada}")