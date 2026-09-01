# Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

valor = int(input("Digite um numero para saber sua tabuada completa: "))
for numero in range (1):
    for multiplicador in range(1,11):
        tabuada = valor * multiplicador
        print(f"{valor} x {multiplicador} = {tabuada}")