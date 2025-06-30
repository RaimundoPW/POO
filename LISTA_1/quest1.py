
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
      


#METODOS
    def descrever(self):
        print(f"Marca: {self.marca} {self.modelo} {self.ano}")



#CRIANDO OBJETOS:
c1 = Carro("Toyota", "Corolla",2025)
c2 = Carro("KOA", "Tiggo",2025)

#CHAMANDO UM MÉTODO!
c1.descrever()
c2.descrever()