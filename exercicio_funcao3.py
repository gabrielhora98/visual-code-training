saldo = 100
def adicionar_dinheiro(valor):
    global saldo
    saldo = saldo + valor
    return saldo 

print(adicionar_dinheiro(50))

print(saldo)