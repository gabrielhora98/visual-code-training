#   funções reutilizáveis
#saldo = 100
#def calcular_saldo(saldo, valor, operacao):
#    if operacao == "D":
#        resultado = saldo + valor
#    elif operacao == "S":
#            resultado = saldo - valor
#    else:
#        print("Tente a letra da operacao correta.")
#        return "erro"
#    return resultado
#print(calcular_saldo(saldo, 50, "S"))
#print(calcular_saldo(saldo, 30, "D"))
#print(calcular_saldo(saldo, 50, "x"))
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#

#   funções que trabalham juntas
#def calcular_desconto(preco, desconto):
#    resultado = preco * desconto /100
#    return resultado

#def calcular_preco_final(preco, desconto, frete):
#    preco_final = preco - calcular_desconto(preco, desconto)
#    resultado = frete + preco_final
#    return resultado

#print(calcular_preco_final(500, 20, 15))
#print(calcular_desconto(500, 20))
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#
