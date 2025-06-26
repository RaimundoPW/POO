#Adicione um metodo chamado ligar() que imprime "O carro {modelo} está ligado."

class Carro:
    def __init__(self, modelo):
        
        self.modelo = modelo
        

#METODOS
    def ligar(self):
        print(f"O carro modelo {self.modelo} está ligado.")

#CRIANDO OBJETOS:
c1 = Carro("Hb20")

#CHAMANDO UM MÉTODO!
c1.ligar()
       