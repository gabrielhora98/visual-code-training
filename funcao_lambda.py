# Função lambda 
# função anônima e curta usada para realizar uma
# operação simples, geralmente em uma única expressão.

# funcao normal
# def dobrar(numero):
#    return numero * 2

# funcao lambda 
# dobrar = lambda numero: numero * 2

# exercicio 1
# quadrado = lambda numero: numero**2
# print(quadrado(5))

# exercicio 2 
# para mostrar o numero na condicao lambda como se eu quisesse chamar o print,
# eu coloco o primeiro parametro na frente da condicao. 

# primeiro chamo LAMBDA e coloco os dois parametros (numero1 e numero2)
# depois coloco numero1 como se fosse um return(numero1) se a condicao for verdadeira
# depois faço a condicao que eu quero e no final do else eu coloco o numero2 para retornar
# caso a condicao for falsa.
maior = lambda numero1, numero2: numero1 if numero1 > numero2 else numero2
print(maior(10,7))