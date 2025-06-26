
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
      


#METODOS
    def apresentar(self):
        print(f"Olá, esse é o {self.marca} {self.modelo} {self.ano}")



#CRIANDO OBJETOS:
c1 = Carro("Toyota", "Corolla",2025)
c2 = Carro("KOA", "Tiggo",2025)

#CHAMANDO UM MÉTODO!
c1.apresentar()
c2.apresentar()