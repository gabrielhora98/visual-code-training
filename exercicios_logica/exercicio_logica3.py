#  Faça um algoritmo que leia dois valores inteiros A e B,
#  se os valores de A e B forem iguais, deverá somar os dois valores,
#  caso contrário devera multiplicar A por B. Ao final de qualquer um dos 
# cálculos deve-se atribuir o resultado a uma variável C eimprimir seu valor na tela

a = int(input("digite um valor: "))
b = int(input("digite um segundo valor: "))

if a == b:
   c = a + b
   print(c)
else:
   c = a * b
   print(c)
    