def pessoa(**kwargs):
    print(kwargs)

pessoa(nome="nicoly", idade = 26, cidade = "Rj", pais = "Brasil")
pessoa(nome ="gabriel", idade = 28, cidade = "sao paulo", pais = "Brasil")

print(pessoa)

# o arguento (**kwargs) é usado para "criar" um dicionario.  