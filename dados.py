import csv
from aluno import Aluno

class Dados:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.alunos = []

    def lerDados(self):
        with open(self.arquivo) as alunosDados:
            csvReader = csv.reader(alunosDados, delimiter=",")
            for aluno in csvReader:
                alunoClasse = Aluno(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5])
                self.alunos.append(alunoClasse)

    def attUffmail(self, aluno):
        alunosDadosAtt = open("dados/alunos_att.csv", "w")
        csvWriter = csv.writer(alunosDadosAtt)

        with open(self.arquivo) as alunosDados:
            csvReader = csv.reader(alunosDados, delimiter=",")

            for linha in csvReader:
                if linha[1] == aluno.matricula:
                    linha[4] = aluno.uffmail
                csvWriter.writerow(linha)
                
    