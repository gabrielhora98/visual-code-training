# Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago,
# conforme a escolha da forma de pagamento pelo comprador e
# imprima na tela o valor final do produto a ser pago.
# Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
# Tabela de Código de Condições de Pagamento
#1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
#2 - À Vista no cartão de crédito, recebe 10% de desconto
#3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
#4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%

produto = float(input("Digite o valor do produto: R$ "))

while True:
    print("1 - À Vista em Dinheiro ou Pix ")
    print("2 - À Vista no cartão de crédito")
    print("3 - Parcelado no cartão em duas vezes")
    print("4 - Parcelado no cartão em três vezes ou mais")
    print("5 - Sair")
    opcao = input("Escolha uma forma de pagamento: ").strip()

    if opcao == "1":
        valor_final = produto - ((produto * 15) / 100 )
        #valor_final = produto - (produto * 0.15) 
        #tambem pode fazer dessa forma a portentagem. só transformar em decimal.
        print(f"R$ {valor_final}")
        break
    elif opcao == "2":
        valor_final = produto - ((produto * 10) / 100)
        print(f"R$ {valor_final}")
        break
    elif opcao == "3":
        print(f"R$ {produto}")
        break
    elif opcao == "4":
        valor_final = produto + ((produto *10) / 100)
        print(f"R$ {valor_final}")
        break
    elif opcao == "5":
        print("Operaçao cancelada.")
        exit()
    else:
        print("Opçao invalida.")