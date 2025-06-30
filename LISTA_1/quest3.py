#Crie 2 objetos da classe "Carro" e utilize os dois métodos.


class Carro:
    def __init__(self, marca, modelo):
        self.marca  = marca
        self.modelo = modelo
       

#METODOS
    def ligar(self):
        print(f"O carro modelo {self.marca} {self.modelo} esta pronto para ligar")

    def buzinando(self):
        print(f"O carro modelo {self.marca} {self.modelo} está Biiiiiip Biiiiip")



#CRIANDO OBJETOS:
c1 = Carro("Toyota", "Corolla")
c2 = Carro("Hyunday", "Creta") 

#CHAMANDO UM MÉTODO!
c1.ligar()
c2.buzinando()