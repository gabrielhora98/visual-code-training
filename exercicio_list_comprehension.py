# list comprehension É uma forma mais curta e prática 
# de criar novas listas a partir de outra lista, podendo transformar ou filtrar valores.



#numeros = []

#or numero in range(1,11):
#    numeros.append(numero)
#    print(numero)

#print(numeros)

#numeros_par = [numero for numero in numeros if numero % 2 == 0]
#print(numeros_par)

##################################################################

numeros = [1,2,3,4,5,6,7,8,9,10]

pares_em_dobro = [numero*2 for numero in numeros if numero % 2 == 0 ]
print(pares_em_dobro)