# Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias
# essa pessoa ja viveu. Leve em consideração o ano com 365 dias e o mês com 30 dias.
# (Ex: 5 anos, 2 meses e 15 dias de vida)

ano_nascimento = int(input("Digite sua data de nascimento: "))
mes_nascimento = int(input("Digite seu mes de nascimento: "))
dia_nascimento = int(input("Digite seu dia de nascimento: "))

ano_atual = 2026
mes_atual = 8
dia_atual = 26


dias_nascimento = (ano_nascimento * 365) + (mes_nascimento * 30) + dia_nascimento

dias_atual = (ano_atual * 365) + (mes_atual * 30) + dia_atual

idade_em_dias = dias_atual - dias_nascimento

anos = idade_em_dias // 365
resto = idade_em_dias % 365

meses = resto // 30
dias = resto % 30

print(f"{anos} anos, {meses} meses e {dias} dias de vida.")