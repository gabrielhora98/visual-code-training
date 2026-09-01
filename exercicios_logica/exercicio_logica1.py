# Faça um algoritmo que leia os 
# valores de A, B, C e em seguida imprima
# na tela a soma entre A e B é mostre se a soma é menor que C.

valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
valor3 = int(input("digite o terceiro valor: "))

soma = valor1 + valor2 
print(soma)

if soma > valor3:
    print(f"a soma {soma} é maior.")
else:
    print("o valor3 é maior que a soma.")