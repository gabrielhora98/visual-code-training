# Faça um algoritmo que leia três valores que representam
# os três lados de um triângulo e verifique se são válidos, 
# determine se o triângulo é equilátero, isósceles ou escaleno.

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 + lado2 > lado3 and lado3 + lado2 > lado1 and lado1 + lado3 > lado2:
    if lado1 == lado2 and lado3 == lado2:
        print("Esse triangulo é equilátero!")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Esse triangulo é isósceles!")
    else:
        print("Esse triangulo é escaleno!")
else:
    print("Os valores nao formam um triangulo")