# Faça algoritmo que leia o nome e a idade de uma pessoa
#  e imprima na tela o nome da pessoa e se ela é maior ou menor de idade.

print("Me fale seu nome e sua idade.")
nome = input("Nome: ")
idade = int(input("Idade: "))

if idade > 18:
    print(f"{nome} voce é maior de idade")
else:
    print(f"{nome} voce é menor de idade")
    