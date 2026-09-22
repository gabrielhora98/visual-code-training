#nome_longo = lambda nome: "nome longo" if len(nome) > 5 else "nome curto"

#print(nome_longo("Gabr"))

###########################################################################

produtos = [
    {"nome": "Camisa", "preco": 50},
    {"nome": "Calça", "preco": 80},
    {"nome": "Casaco", "preco": 30}
]

ordenado = sorted(produtos, key=lambda produto: produto ["preco"])
print(ordenado)
