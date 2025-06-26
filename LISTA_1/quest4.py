
#Crie uma classe (ALUNO) com atributos NOME, NOTAS, uma lista de 3 notas. Adicione um metodo 
#chamado MÉDIA() que retorna a média das notas.

class aluno:
    def __init__ (self, nome, notas):
        self.nome = nome
        self.notas = notas


    def media(self):
        media = sum(self.notas) / 3
        print(f"O aluno {self.nome} média dele é {media}")




notas = [6, 8, 7]
aluno1 = aluno("Gilmar", notas)

aluno1.media()

