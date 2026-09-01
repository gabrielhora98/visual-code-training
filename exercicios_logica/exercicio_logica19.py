# Faça um algoritmo que imprima na tela a tabuada de 1 até 10.
for numero in range(1, 11):
    for multiplicador in range(1, 11):
        tabuada = numero * multiplicador
        print(f"{numero} x {multiplicador} = {tabuada}")