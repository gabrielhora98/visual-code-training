# Faça um algoritmo que leia dois valores booleanos (lógicos)
# e determine se ambos são VERDADEIRO ou FALSO.

dia = (input("Hoje é domingo? S/N: ")).upper()

if dia == "n":
    dia = False
else:
    dia = True

mes = (input("Estamos em agosto? S/N: ")).upper()

if mes == "n":
    mes = False
else:
    mes = True

if dia == True and mes == True:
    print("Voce acertou o dia e o mes!")
else:
    print("Voce errou!")

