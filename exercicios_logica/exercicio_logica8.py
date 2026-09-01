# Faça um algoritmo que leia três valores inteiros 
# diferentes e imprima na tela os valores em ordem decrescente.
numeros = []
for pergunta in range(3):
    numeros.append(int(input("Digite um numero: ")))

print(sorted(numeros, reverse= True))
