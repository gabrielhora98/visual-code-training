class Livro:
    def __init__(self, titulo, autor): # se usa o __init__ para criar atributos da classe. 
        self.titulo = titulo           #self serve para representar o proprio objeto que chamou o metodo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso.")
        else:
            print(f"O livro {self.titulo} não esta disponivel para emprestimo.")
    
    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido com sucesso.")
        else:
            print(f"Esse livro ja esta disponivel em nosso estoque")

    def mostrar_status(self):
        if self.disponivel:
            status = "Disponivel"
        else:
            status = "Emprestado"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Status: {status}")

    
livro1 = Livro("phyton", "Gabriel Hora")
livro2 = Livro("viva a mata", "cacado ")


livro2.mostrar_status()
livro1.mostrar_status()
livro2.emprestar() 
livro1.emprestar()
