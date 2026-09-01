class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print("O veiculo esta ligado")

class Carro(Veiculo):
    def ligar(self): #repetir o def ligar é uma sobreposição para alterar a funçao somente para a classe carro.
        print("O carro esta ligado e com o farol acesso.")

    def abrir_porta(self):
        print("O carro esta de porta aberta")


class Moto(Veiculo):
    def empinar(self):
        print("A moto empinou")

    def ligar(self):   #aqui eu usei o super() para usar a funçao da classe principal e adicionar mais um print
        super().ligar()
        print("Ligou o farol")



moto1 = Moto("Honda", "Fan 160")

carro1 = Carro("chev", "prisma")

carro1.ligar()
carro1.abrir_porta()

moto1.ligar()
moto1.empinar()