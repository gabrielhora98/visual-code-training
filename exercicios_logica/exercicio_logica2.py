# Faça um algoritmo para receber um número qualquer e 
# imprimir na tela se o número é par ou ímpar, positivo ou negativo.

num1 = int(input("digite um numero: "))

if num1 % 2 == 0:
    print("é par")
else:
    print("é impar")

if num1 > 0:
    print(f"o {num1} é positivo")
else:
    print(f"o {num1} é negativo")
