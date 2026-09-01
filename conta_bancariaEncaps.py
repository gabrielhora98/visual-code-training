class Conta_bancaria:
    def __init__(self, titular):
        self.__titular = titular  #__ privado = voce nao deve mexer nunca
        self.__saldo = 0          #_ protegido = voce nao deveria mexer nisso

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido. Tente valor acima de 0.")

    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print("Não foi possivel sacar esse valor")

    def mostrar_saldo(self):
        print(f"Titular: {self.__titular}")
        print(f"Saldo: R${self.__saldo}")


conta1 = Conta_bancaria("Gabriel")
conta1.depositar(200)
conta1.sacar(50)
conta1.mostrar_saldo()
conta1.sacar(500)
conta1.mostrar_saldo()
