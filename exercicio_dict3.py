produtos = []
                                            
def cadastrar_produto():
    while True:
        while True:
            nome = input("Digite o nome do produto: ").upper().strip()
            if nome == "":
                print("Nome inválido. O nome do produto não pode ser vazio.")
            else:
                break
        while True:
            try:
                preço = float(input("Digite o preço do produto: "))
                if preço <= 0:
                    print("Preço inválido. O preço não pode ser zero ou negativo.")
                else:
                    break
            except ValueError:
                print("Preço inválido. Digite um número válido.")
        while True:
            try:
                quantidade = int(input("Digite a quantidade do produto: "))
                if quantidade <= 0:
                    print("Quantidade inválida. A quantidade não pode ser zero ou negativa.")
                else:
                    break
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro válido.")
        while True:
            tamanho = input("Digite o tamanho do produto: ").upper().strip()
            if tamanho == "":
                print("Tamanho inválido. O tamanho do produto não pode ser vazio.")
            else:
                break
        encontrado = False
        for produto in produtos:
            if nome == produto['nome'] and tamanho == produto['tamanho']:
                print("Produto já cadastrado!")
                encontrado = True
                while True:
                    resposta = input("Deseja adicionar a quantidade ao estoque? (S/N): ").upper().strip()
                    if resposta == "S":
                        while True:
                            try:
                                quantidade_adicional = int(input("Digite a quantidade que deseja adicionar: "))
                                if quantidade_adicional <= 0:
                                    print("Quantidade inválida. A quantidade adicional não pode ser zero ou negativa.")
                                else:
                                    break
                            except ValueError:
                                print("Quantidade inválida. Digite um número inteiro válido.")
                        produto['quantidade'] += quantidade_adicional
                        print(f"Estoque atualizado. Nova quantidade de {produto['nome']}: {produto['quantidade']}")
                        break
                    elif resposta == "N":
                        print("Ok, o produto não foi alterado.")
                        break 
                    else:
                        print("Opção inválida.")   
        
        if not encontrado:                    
            produto = {"nome": nome,
                        "preço": preço,
                        "quantidade": quantidade,
                        "tamanho": tamanho}
            produtos.append(produto)
            print(f"Produto {nome} cadastrado com sucesso!")
        sair = False
        while True:
            cadastro = input("Deseja cadastrar outro produto? (S/N): ").upper().strip()
            if cadastro == "N":
                sair = True
                print("Voltando ao menu principal...")
                break
            elif cadastro == "S":
                break
            else:
                print("Opção inválida.")
        if sair:
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
    while True:
        nome_procurado = input("Digite o nome do produto que deseja adicionar estoque: ").upper().strip()
        if nome_procurado == "":
            print("Nome inválido. O nome do produto não pode ser vazio.")
        else:
            break
    while True:
        tamanho_procurado = input("Digite o tamanho do produto que deseja adicionar estoque: ").upper().strip()
        if tamanho_procurado == "":
            print("Tamanho inválido. O tamanho do produto não pode ser vazio.")
        else:
            break

    encontrado = False
    for produto in produtos:
        if nome_procurado == produto["nome"].upper() and tamanho_procurado == produto['tamanho'].upper().strip():
            while True:
                try:
                    quantidade_adicional = int(input("Digite a quantidade que deseja adicionar: "))
                    if quantidade_adicional <= 0:
                        print("Quantidade inválida. A quantidade adicional não pode ser zero ou negativa.")
                    else:
                        break
                except ValueError:
                    print("Quantidade inválida. Digite um número inteiro válido.")
            produto["quantidade"] += quantidade_adicional
            print(f"Estoque atualizado. Nova quantidade de {produto['nome']}: {produto['quantidade']}")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado.")

def retirar_estoque():
    while True:  
        nome_procurado = input("Digite o nome do produto que deseja retirar do estoque: ").strip().upper()
        if nome_procurado == "":
            print("Nome inválido. O nome do produto não pode ser vazio.")   
        else:
            break
    while True:
        tamanho_procurado = input("Digite o tamanho do produto que deseja retirar do estoque: ").strip().upper()
        if tamanho_procurado == "":
            print("Tamanho inválido. O tamanho do produto não pode ser vazio.")
        else:
            break
    encontrado = False
    for produto in produtos:
        if nome_procurado == produto['nome'].upper() and tamanho_procurado == produto['tamanho'].upper():
            while True:
                try:
                    quantidade_retirada = int(input("Digite a quantidade que deseja retirar: "))
                    if quantidade_retirada <= 0:
                        print("Quantidade inválida. A quantidade a ser retirada não pode ser zero ou negativa.")
                    else:
                        break
                except ValueError:
                    print("Quantidade inválida. Digite um número inteiro válido.")
            if quantidade_retirada <= produto['quantidade']:
                produto['quantidade'] -= quantidade_retirada
                print(f"Estoque atualizado. Nova quantidade de {produto['nome']}: {produto['quantidade']}")
                encontrado = True
                break
            else:
                print("Quantidade insuficiente em estoque.")
                encontrado = True
                break            
    if not encontrado:
        print("Produto não encontrado.")

def editar_produto():
    while True:
        nome_procurado = input("Digite o nome do produto que deseja editar: ").strip().upper()
        if nome_procurado == "":
            print("Nome inválido. O nome do produto não pode ser vazio.")
        else:
            break
    while True:
        tamanho_procurado = input("Digite o tamanho do produto que deseja editar: ").strip().upper()
        if tamanho_procurado == "":
            print("Tamanho inválido. O tamanho do produto não pode ser vazio.")
        else:
            break
    encontrado = False
    for produto in produtos:
        if nome_procurado == produto['nome'].upper() and tamanho_procurado == produto['tamanho'].upper():
            novo_nome = input("Digite o novo nome do produto: ").strip().upper()
            while True:
                try:
                    novo_preco = float(input("Digite o novo preço do produto: "))
                    if novo_preco <= 0:
                        print("Preço inválido. O preço não pode ser zero ou negativo.")
                    else:
                        break
                except ValueError:
                    print("Preço inválido. Digite um número válido.")
            while True:
                novo_tamanho = input("Digite o novo tamanho do produto: ").strip().upper()
                if novo_tamanho == "":
                    print("Tamanho inválido. O tamanho do produto não pode ser vazio.")
                else:
                    break
            produto['nome'] = novo_nome
            produto['preço'] = novo_preco
            produto['tamanho'] = novo_tamanho
            print("Produto atualizado com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.")

while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Deletar produto")
    print("4 - Buscar produto")
    print("5 - Adicionar estoque")
    print("6 - Retirar estoque")
    print("7 - Sair")
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
        retirar_estoque()
    elif opcao == "7":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
