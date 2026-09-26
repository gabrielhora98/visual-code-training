#def somar(*args):
#    total = 0                  o (*args) é para receber varios argumentos na funçao
#    for numero in args:
#        total += numero
#    return total
#print(somar(10,50,30))
#print(somar(30,20))
                                # o sum(args) é uma funcao que soma todos os parametros
def somar(*args):
    return sum(args)    
print(somar(10,30,40,20))