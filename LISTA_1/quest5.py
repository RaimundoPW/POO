#(DESAFIO) Adicione um método  chamado "situacão()" que diz se o aluno
# está "Aprovado" (média >= 7) ou "Reprovado". 

class Aluno:
    def __init__(self,nome, notas, media,):
        
        self.notas = notas
        self.media = media
        self.nome = nome

#METODOS
    def notas(self):
        print(f"A media do aluno é {self.notas} aluno aprovado {self.media}")

    def situacao(self):
         print(f"O aluno  {self.notas} aluno aprovado {self.media}")



#CRIANDO OBJETOS:

aluno = Aluno("Gilmar",)

#CHAMANDO UM MÉTODO!
aluno1.situacao()