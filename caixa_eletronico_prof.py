def boas_vindas():
    print("==== Bem-vindo ao Banco Hora! ====") 
boas_vindas()

saldo = 1000
usuario = "iris123"
senha = "1234"
tentativas = 0
historico = []

def login_usuario(login, senha_digitada):
        return login == usuario and senha_digitada == senha

while True:
    login = input("digite seu login: ")
    senha_digitada = input("Digite sua senha: ")
    aprovado = login_usuario(login, senha_digitada)
    if aprovado == True:
         print("Login realizado com sucesso!")
         break
    else:
        tentativas += 1
        if tentativas >= 3:
            print("Conta bloqueada.")
            exit()
        else:
            print("Login ou senha incorretos. Tente novamente.")
            print(F"Você tem {3 - tentativas} tentativas restantes.")

def depositar(saldo, deposito, historico):
    if deposito > 0:
        saldo += deposito
        historico.append(F"Depósito: R$ {deposito}")
    return saldo

def sacar(saldo, saque, historico):
    if saque > 0 and saque <= saldo:
        saldo -= saque
        historico.append(F"Saque: R$ {saque}")
    return saldo


def menu():
 global saldo

 while True:
    print("==== Menu ====")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Histórico de transações")
    print("5. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(F"Seu saldo atual é: R$ {saldo}")
    
    elif opcao == 2:
        print("Quanto deseja depositar?") 
        deposito = float(input("R$: "))
        if deposito > 0:
            saldo = depositar(saldo, deposito, historico)
            print(F"Seu saldo atual é: R$ {saldo}")
        else:
            print("Valor inválido. Tente novamente.")
    elif opcao == 3:
        print("Quanto deseja sacar?")
        saque = float(input("R$: "))
        if saque <= 0:
            print("Valor inválido. Tente novamente.")
        elif saque > saldo:
            print("Saldo insuficiente. Tente novamente.")
        else:
            saldo = sacar(saldo, saque, historico)
            print(F"Seu saldo atual é: R$ {saldo}")
    elif opcao == 4:
        print("=== Historico de transações! ===")
        if historico == []:
            print("Nenhuma transação feita.")
        else:
            for transacao in historico:
              print(transacao)
    elif opcao == 5:
        print("Obrigado por utilizar nosso sistema bancário. Volte sempre!")
        exit()    
    else:
        print("Opção inválida. Tente novamente!")

 
menu()
