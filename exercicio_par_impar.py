print("vamos descobrir se o numero é par ou impar, quantos numeros de cada e qual é o maior e o menor.")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))
num5 = int(input("Digite o quinto numero: "))

par = 0
impar = 0
maior_atual = num1
menor_atual = num1

numeros = [num1, num2, num3, num4, num5]
for numero in numeros:
    if numero % 2 == 0:
        par += 1 
    else:
        impar += 1
    if numero > maior_atual:
        maior_atual = numero

    if numero < menor_atual:
        menor_atual = numero


print(f"Par: {par}")
print(f"Impar: {impar}")
print(f"Maior numero: {maior_atual}")
print(f"Menor numero: {menor_atual}")
