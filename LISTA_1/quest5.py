#(DESAFIO) Adicione um método  chamado "situacão()" que diz se o aluno
# está "Aprovado" (média >= 7) ou "Reprovado". 

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 7:
            return "Aprovado(a)"
        else:
            return "Reprovado"

# Exemplo de uso:
aluno1 = Aluno("Gilmar", 7.6, 6.2)
print(f"{aluno1.nome} está {aluno1.situacao()} com média: {aluno1.media():.1f}")
