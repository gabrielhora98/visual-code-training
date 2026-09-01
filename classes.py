class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def Informacoes_do_carro(self):
        print(self.marca, self.modelo,self.ano)
    
    def ligar(self):
        print("estou ligando.")

    def andar(self):
        print("estou andando.")
    
    def freiar(self):
        print("estou freiando.")
    
    def estacionar(self):
        print("estacionando o carro.")
    
carro1 = Carro("Chev", "Prisma", "19")
carro1.Informacoes_do_carro()
carro1.ligar()
carro1.andar()
carro1.freiar()
carro1.estacionar()
