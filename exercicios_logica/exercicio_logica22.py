# Faça um algoritmo que leia dois valores inteiros A e B,
# imprima na tela o quociente e o resto da divisão inteira entre eles.

a = int(input("digite um valor: "))
b = int(input("digite um valor para dividir o anterior: "))

quociente = a // b
resto = a % b
print(f"o quociente é {quociente} e o resto é {resto}")
