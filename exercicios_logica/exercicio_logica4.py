#Faça um algoritmo que receba um número inteiro 
# e imprima na tela o seu antecessor e o seu sucessor.
a = int(input("digite um numero: "))

sucessor = a + 1

antecessor = a - 1

print(f" {antecessor} < {a} < {sucessor}")