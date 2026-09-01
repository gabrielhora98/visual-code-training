class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def trabalhar(self):                                    # Polimorfismo é quando utilizo a mesma função em classes
        print("O funcionario esta trabalhando.")            # e o resultado é diferente.

class Programador(Funcionario):
    def trabalhar(self):
        print(f"{self.nome } esta escrevendo código.")

class Designer(Funcionario):
    def trabalhar(self):
        print(f"{self.nome} esta criando layout.")

class Gerente(Funcionario):
    def trabalhar(self):
        print(f"{self.nome} esta gerenciando a equipe.")


funcionarios = [Programador("biel"), Designer("Nicoly"), Gerente("Iris")]



for listar in funcionarios:
    listar.trabalhar()