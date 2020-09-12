class Aluno:
    def __init__(self, nome, matricula, telefone, email, uffmail, status):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.uffmail = uffmail
        self.status = status
    
    def setUffmail(self, uffmail):
        self.uffmail = uffmail