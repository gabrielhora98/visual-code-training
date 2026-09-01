####  RPG EM PYTHON ####
"""
RPG em Python

Objetivo:
Praticar Programação Orientada a Objetos.

Conceitos utilizados:
- Classes
- Objetos
- Herança
- Polimorfismo
- Encapsulamento
- super()
- random
- for
- while
- if/elif/else
- Métodos
- Atributos
- Listas de objetos
- Sistema de batalha
- Sistema de XP
- Level Up
"""



import random


print("Qual é o nome do seu personagem?")
nome = input(" ")
print(f"Seja bem vindo(a) aos 7 reinos {nome}.")

class Personagem:
    def __init__(self, nome):
        self.nome = nome 
        self.vida_maxima = 100
        self.vida = 100 
        self.ataque = 10
        self.defendendo = False 
        self.pocoes = 3
        self.nivel = 1
        self.xp = 0
        self.xp_proximo_nivel = 100

    def atacar(self,inimigo):
        numero_sorteado = random.randint(1,10)
        if numero_sorteado <= 2:
            dano = 0
            print(f"{self.nome} errou o ataque!")
        elif numero_sorteado >= 9:
            dano = self.ataque * 2
            print(f"{self.nome} acertou um ataque crítico de {dano} de dano!")        
        else:
            dano = self.ataque

        if dano > 0:
            inimigo.receber_dano(dano)  

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} entrou em modo de defesa!")

    def mostrar_status(self):
        print(f"Nome:{self.nome}")
        print(f"Vida:{self.vida}/{self.vida_maxima}")
        print(f"Ataque:{self.ataque}")

    def receber_dano(self, dano):
        if self.defendendo == True:
            dano = dano // 2
            self.vida -= dano
            self.defendendo = False
        else:
            self.vida -= dano

        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} recebeu {dano} de dano.")
            print(f"{self.nome} agora tem {self.vida} de vida.")

    def usar_pocao(self):
        if self.vida < self.vida_maxima:
            if self.pocoes > 0:
                self.pocoes -= 1
                print(f"Poções restantes: {self.pocoes}")
                self.vida += 20
                if self.vida > self.vida_maxima:
                    self.vida = self.vida_maxima
                print(f"{self.nome} usou uma poção de cura!")
                print(f"{self.nome} agora tem {self.vida} de vida.")
            else:
                print("Você não tem mais poções de cura!")
        else: 
            print(f"{self.nome} já está com a vida cheia e não pode usar a poção de cura.")

    def receber_xp(self, xp): 
        self.xp += xp
        while self.xp >= self.xp_proximo_nivel:
            self.nivel += 1
            self.ataque += 5
            self.vida_maxima += 10
            self.vida = self.vida_maxima
            self.xp -= self.xp_proximo_nivel
            print(f"{self.nome} subiu para o nível {self.nivel}!")
            self.xp_proximo_nivel = int(self.xp_proximo_nivel * 1.5)

        print(f"{self.nome} recebeu {xp} de experiência!")
        print(f"xp atual: {self.xp}/{self.xp_proximo_nivel}")
        

class Guerreiro(Personagem):
    def __init__(self,nome):
        super().__init__(nome)
        self.ataque = 20

    def atacar(self,inimigo):
        print(f"{self.nome} sacou a espada e golpeou o inimigo!")
        super().atacar(inimigo)

    def defender(self):
        print(f"{self.nome} puxou seu escudo.")
        super().defender()

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.ataque = 40

    def atacar(self,inimigo):
        print(f"{self.nome} concentrou-se e usou seu feitiço para atingir o inimigo!")
        super().atacar(inimigo)

    def defender(self):
        super().defender()
        print(f"{self.nome} usou sua magia para se proteger")

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.ataque = 30

    def atacar(self,inimigo):
        print(f"{self.nome} puxou seu arco e atirou uma flecha no inimigo!")
        super().atacar(inimigo)


class Inimigo(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.vida = 60  
        self.ataque = 8
        self.xp = 10

    def atacar(self,personagem):
        print(f"{self.nome} atacou!")
        super().atacar(personagem)

    def defender(self):
        print(f"{self.nome} se defendeu!")


class Goblin(Inimigo):
    def __init__(self,): 
        super().__init__("Goblin")
        self.xp = 10
        self.vida = 50
        self.vida_maxima = 50

class Orc(Inimigo): 
    def __init__(self):
        super().__init__("Orc")
        self.vida = 100
        self.vida_maxima = 100
        self.ataque = 15 
        self.xp = 20

class Esqueleto(Inimigo):
    def __init__(self):
        super().__init__("Esqueleto")
        self.vida = 80
        self.vida_maxima = 80
        self.ataque = 12
        self.xp = 15
class Orc_chefe(Inimigo): 
    def __init__(self):
        super().__init__("Orc")
        self.vida = 150
        self.vida_maxima = 150
        self.ataque = 20 
        self.xp = 60

while True:
    print("== Escolha sua classe ==")
    print("1 - Guerreiro")
    print("2 - Mago")
    print("3 - Arqueiro")
    opcao = input("Qual personagem você deseja jogar?: ")

    if opcao == "1":
        personagem = Guerreiro(nome)
        print("Você foi escolhido como o guerreiro campeão da cidade da campos.")
        personagem.mostrar_status()
        break

    elif opcao == "2":
        personagem = Mago(nome)
        print("Você foi escolhido como o mago mais poderoso dos 7 reinos.")
        personagem.mostrar_status()
        break

    elif opcao == "3":
        personagem = Arqueiro(nome)
        print("você foi designado a caça como o arqueiro mais destemido dos 7 reinos.")
        personagem.mostrar_status()
        break
    else:
        print("Opção inválida. Esolha novamente.")


game_over = False
for fase in range(1, 5):
        if game_over:
            break        
        print(f"\n========== FASE {fase} ==========")
        if fase == 1:
            inimigos = [Goblin()]
        elif fase == 2:
            inimigos = [Goblin(), Esqueleto()]
        elif fase == 3:
            inimigos = [Orc(), Esqueleto()]
        else: 
            inimigos = [Orc_chefe()]
            print("Você encontrou o chefe da fase final! Prepare-se para a batalha!")
          
        
        inimigo = random.choice(inimigos)
        print(f"Um {inimigo.nome} apareceu!")
        inimigo.mostrar_status()
        
        while True:
            print("1 - Atacar")
            print("2 - Defender")
            print("3 - usar poção de cura")
            print("4 - Mostrar status")
            print("5 - Fugir")
            acao = input("O que você deseja fazer?: ")

            if acao == "1":
                personagem.atacar(inimigo)
                if inimigo.vida > 0:
                    inimigo.atacar(personagem)
                    if personagem.vida <= 0:
                        game_over = True
                        print("Game Over! Você foi derrotado!")
                        break
                else:
                    personagem.receber_xp(inimigo.xp)
                    print("Você derrotou o inimigo!")
                    print("Fim da batalha!")
                    break

            elif acao == "2":
                personagem.defender()
            elif acao == "3":
                personagem.usar_pocao()
                
            elif acao == "4":
                personagem.mostrar_status()
                inimigo.mostrar_status()
            elif acao == "5":
                print("Você fugiu!")
                break
            else:
                print("Opção inválida.")
        