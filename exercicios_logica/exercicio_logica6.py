#Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.

salario_atual = float(input("Digite seu salario: "))
aumento = salario_atual * 0.05 
salario_novo = salario_atual + aumento
print(salario_novo)