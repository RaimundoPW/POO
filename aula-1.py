#Criando uma classe em POO!

class Pessoa:
    def __init__(self, nome, idade,peso, raça):
        self.nome = nome
        self.idade = idade 
        self.peso = peso
        self.raça = raça


#METODOS
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos, meu peso é {self.peso} minha raça é {self.raça}")



#CRIANDO OBJETOS:
p1 = Pessoa("Gilmar",50,70,("indio"))
p2 = Pessoa("Jayme",40,70, ("branco"))

#CHAMANDO UM MÉTODO!
p1.apresentar()
p2.apresentar()
