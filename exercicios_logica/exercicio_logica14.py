# Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e 
# o valor de B por A e imprima na tela os valores.
print("Vou trocar os valores que voce escolher.")

valor_a = int(input("digite um valor: "))
valor_b = int(input("digite outro valor: "))

temporario = valor_a
valor_a = valor_b
valor_b = temporario

print(valor_a)
print(valor_b)