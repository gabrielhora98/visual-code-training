# Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

print("Vamos ver sua media escolar.")

nota1 = float(input("digite sua primeira nota:"))
nota2 = float(input("digite sua segunda nota:"))
nota3 = float(input("digite sua terceira nota:"))

media = (nota1 + nota2 + nota3) / 3
print(f"sua media escolar é {media}")