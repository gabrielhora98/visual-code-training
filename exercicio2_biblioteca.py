estoque = ["Percy Jackson" , "Harry Potter 1" , "Harry Potter 2"]
print("=== Bem vindo a biblioteca do Hora! ===")
if estoque == []:
    print("Não há livros disponíveis.")

def cadastrar_livro(estoque):
    print("Qual livro você quer adicionar?")
    livro = input("Digite o nome do livro: ")
    estoque.append(livro)
    print(f"O {livro} foi cadastrado com sucesso!")


def retirar_livro(livro,estoque):
    if livro in estoque :
        estoque.remove(livro)
        print(f"O livro {livro} foi retirado com sucesso.")
    else:
        print(f"O livro {livro} nao tem em nosso estoque.")

            


    
def biblioteca (estoque):
    for biblioteca in estoque:
        print(biblioteca)



def menu ():
    while True:
        print("1 - Cadastrar livros.")
        print("2 - Retirar livros.")
        print("3 - Listar livros.")
        print("4 - Sair.")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            cadastrar_livro(estoque)
        elif opcao == 2:
            print("Qual o nome do livro voce deseja retirar?")
            livro = input("Digite o nome do livro: ")
            print(f"Tem certeza que deseja retirar o livro {livro}?")
            resposta = input("S/N?: ").upper()
            if resposta == "S":
                retirar_livro(livro,estoque)
            elif resposta == "N":
                print(f"Ok, cancelando retirada do livro {livro}.")
            else:
                print("Algo deu errado. Tente novamente!")
        elif opcao == 3:
            biblioteca(estoque)
        elif opcao == 4:
            exit()
        else:
            print("Opção inválida. Tente novamente!")

menu()
