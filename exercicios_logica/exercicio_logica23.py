# Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, 
# sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será 
# gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros 
# utilizados para fazer a viagem. 
# Fórmula: distância = tempo x velocidade. 
# litros usados = distância / 12.

tempo = float(input("digite o tempo que levou no trajeto da viagem: "))
velocidade = float(input("digite sua velocidade media: "))

distancia = tempo * velocidade
litros_usados = distancia / 12 

print(f"a distancia percorrida na viagem foi de {distancia}km e foram usados {litros_usados} litros de combustivel")