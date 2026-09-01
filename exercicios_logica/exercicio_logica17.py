#Faça um algoritmo que leia uma temperatura em Fahrenheit e 
# calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.
# Fórmula: C = (5 * ( F-32) / 9)

fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
celsius =  (5 * (fahrenheit-32) // 9)
print(f"{celsius} Graus")