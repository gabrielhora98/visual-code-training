class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento
            print("Seu salario aumentou")
        else: 
            print("Esse valor é inválido.")
    
    def diminuir_salario(self, diminuir):
        if diminuir >= self.__salario:
            print("Erro! Nao foi possivel reduzir o salário")
        else:
            self.__salario -= diminuir

    def mostrar_salario(self):
        print(f"Nome: {self.__nome}")
        print(f"Salário: {self.__salario}")

    def obter_salario(self):
        return self.__salario

    
funcionario1 = Funcionario("Gabriel", 3000)
funcionario1.mostrar_salario()

funcionario1.aumentar_salario(500)
funcionario1.mostrar_salario()
funcionario1.diminuir_salario(1000)
funcionario1.mostrar_salario()
funcionario1.diminuir_salario(5000)
funcionario1.mostrar_salario()
