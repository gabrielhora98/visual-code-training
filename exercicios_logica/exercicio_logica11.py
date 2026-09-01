# Faça um algoritmo que leia quatro notas obtidas por um aluno,
# calcule a média das nota obtidas, imprima na tela o nome do aluno e 
# se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado
# sua média final deve ser maior ou igual a 7.

print("Vamos ver sua media e saber se esta aprovado ou nao!")
nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4 
if media >= 7.0:
    print(f"{nome}, voce ficou com a media {media} e esta aprovado!")
else:
    print(f"{nome}, voce ficou abaixo da media com {media} e foi reprovado!")
