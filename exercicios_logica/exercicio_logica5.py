# Faça um algoritmo que leia o valor do salário mínimo e o 
# valor do salário de um usuário, calcule quantos salários mínimos esse 
# usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).
salario_minimo = 1293.20

salario_usuario = float(input("digite seu salario: "))

resultado = salario_usuario / salario_minimo

print(f"o usuario recebe {resultado} salario(s) minimo(s)")
