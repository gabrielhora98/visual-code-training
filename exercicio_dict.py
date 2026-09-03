produto = {"nome": "camisa 1 oficial",
           "preço": "R$ 299,90",
           "quantidade": 3,
           "tamanho": "G"}
print(produto["nome"])
print(produto["preço"])

produto["quantidade"] = 10
produto["tamanho"] = "M"
del produto["preço"]
print(f"quantidade: {produto['quantidade']}")
print(f"tamanho: {produto['tamanho']}") 

produto["categoria"] = "camisa"
print(produto["categoria"])
print(produto["nome"])
print(produto["preço"])