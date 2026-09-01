usuarios = {}

def cadastro_usuario():
     print("vamos criar seu cadastro.")
     login = input("Crie seu login: ")
     senha = input("Crie sua senha: ")
     if login in usuarios:
            print("usuario ja cadastrado.")
     else:
            usuarios[login] = senha
            print("Usuario criado com sucesso!")


def excluir_usuario():
     print("qual usuario voce deseja excluir?")
     login = input("Digite o login para excluir: ")
     print("Tem certeza que deseja excluir esse usuario?")
     resposta = input("S/N?: ").upper()
     if resposta == "S":
          if usuarios == {}:
               print("Não existe nenhum usuario para excluir.")
          elif login in usuarios:
               del usuarios[login]
               print("Usuario excluido com sucesso!")
          else:
               print("Esse usuario nao existe")
     elif resposta == "N":
          print("Ok, cancelaremos a exclusão.")
     else:
          print("Algo deu errado. Tente novamente!")



def alterar_senha():
     print("Ok. Qual usuario deseja alterar a senha?")
     login = input("Digite o login: ")
     if usuarios == {}:
          print("Não existe nenhum usuario para alterar a senha.")
     elif login in usuarios:
          print("Tem certeza que deseja alterar a senha?")
          resposta = input("S/N?: ").upper()
          if resposta == "S":
               senha_nova = input("Digite a senha nova: ")
               usuarios[login] = senha_nova
               print("Senha alterada com sucesso!")
          elif resposta == "N":
               print("Alteração de senha cancelada.")
          else:
               print("Algo deu errado. Tente novamente!")
     else:
          print("Este usuario nao existe.")
     






def acesso_usuario():
      print("Coloque seu login e senha abaixo para entrar na sua conta.")
      login = input("Digite seu login: ")
      senha = input ("Digite sua senha: ")
      if login in usuarios:
           if senha == usuarios[login]:
                print("Acesso liberado!")
           else:
                 print("Acesso negado!")
                 
      else:
            print("Acesso negado!")


def menu():
      while True:
          print("1 - Cadastrar usuario")
          print("2 - Entrar")
          print("3 - Listar usuarios")
          print("4 - excluir usuario")
          print("5 - Sair")
          opcao = int(input("Escolha uma opção: "))
          if opcao == 1:
                cadastro_usuario()

          elif opcao == 2:
                acesso_usuario()

          elif opcao == 3: 
                if usuarios == {}:
                     print("Nenhum usuario cadastrado.")
                else:
                     for listar in usuarios:
                      print(listar)

          elif opcao == 4:
               excluir_usuario()

          elif opcao == 5:
                exit()
          else:
               print("Opção inválida. Tente novamente!")

menu()