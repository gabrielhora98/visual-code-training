def calcular_total(preco, quantidade):
    return preco * quantidade

def verificar_estoque(estoque, quantidade_solicitada):
    return quantidade_solicitada <= estoque 

def calcular_desconto(preco, percentual):
     return preco * percentual / 100

def realizar_venda(preco, quantidade, estoque, percentual):
        if verificar_estoque(estoque, quantidade):
            valor_final = calcular_total(preco, quantidade) 
            return valor_final - calcular_desconto(valor_final, percentual)
        else:
             return False


print(realizar_venda(500, 4, 4, 10))
