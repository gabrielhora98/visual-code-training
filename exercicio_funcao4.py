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
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx#

def verificar_estoque(quantidade, quantidade_minima):
    if quantidade >= quantidade_minima:
        return "Estoque suficiente"
    else:
        return "Estoque baixo"

def vender_produto(estoque, quantidade_venda, quantidade_minima):
    if quantidade_venda <= estoque:
          estoque -= quantidade_venda
          resultado = verificar_estoque(estoque, quantidade_minima)
          print(f"{quantidade_venda} peça(s) vendida(s)")
          return resultado
    else:
         return "Nao tem estoque o suficiente."
    

print(vender_produto(5, 8, 3))