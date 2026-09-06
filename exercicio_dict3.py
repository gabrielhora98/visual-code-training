produtos = []

def cadastrar_produto():
    while True:
        nome = input("Digite o nome do produto: ").upper().strip()
        preço = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        tamanho = input("Digite o tamanho do produto: ").upper().strip()
    
        produto = {"nome": nome,
                    "preço": preço,
                    "quantidade": quantidade,
                    "tamanho": tamanho}
        produtos.append(produto)
    
        cadastro = input("Deseja cadastrar outro produto? (S/N): ").upper().strip()
        if cadastro == "N":
            break
        elif cadastro == "S": 
            continue
        else:
            print("Opção inválida. Voltando ao menu principal.")
            break

def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"Nome: {produto['nome']}")
            print(f"Preço: {produto['preço']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Tamanho: {produto['tamanho']}")
            print("------------------------")


def deletar_produto():
    nome_procurado = input("Digite o nome do produto que deseja deletar: ").upper().strip()
    encontrado = False
    for produto in produtos:
        if nome_procurado == produto["nome"]:
            produtos.remove(produto)
            print(f"Produto {nome_procurado} deletado com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")

def buscar_produto():
    nome_procurado = input("Digite o nome do produto que deseja procurar: ").strip().upper()
    encontrado = False
    produtos_encontrados = 0
    for produto in produtos:
        if nome_procurado in produto["nome"]:
            print(f"Produto encontrado: {produto['nome']}")
            print(f"Preço: {produto['preço']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Tamanho: {produto['tamanho']}")
            print("------------------------")
            encontrado = True
            produtos_encontrados += 1
    if encontrado == False:
        print("Produto não encontrado.")
    else:
        print(f"Total de produtos encontrados: {produtos_encontrados}")

def adicionar_estoque():
    nome_procurado = input("Digite o nome do produto que desea adicionar estoque: ").upper().strip()
    encontrado = False
    for produto in produtos:
        if nome_procurado == produto["nome"].upper():
            quantidade_adicional = int(input("Digite a quantidade que deseja adicionar: "))
            produto["quantidade"] += quantidade_adicional
            print(f"Estoque atualizado. Nova quantidade de {produto['nome']}: {produto['quantidade']}")
            encontrado = True

    if not encontrado:
        print("Produto não encontrado.")

while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Deletar produto")
    print("4 - Buscar produto")
    print("5 - Adicionar estoque")
    print("6 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        deletar_produto()
    elif opcao == "4":
        buscar_produto()
    elif opcao == "5":
        adicionar_estoque()
    elif opcao == "6":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
