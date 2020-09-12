from aluno import Aluno
from dados import Dados

def geraEmails(nome):
    emails = []
    dom = "@id.uff.br"
    nomes = nome.split()
    emails.append(nomes[0] + "_" + nomes[1] + dom)
    emails.append(nomes[0] + nomes[1][0] + nomes[2][0] + dom)
    emails.append(nomes[0] + nomes[2] + dom)
    emails.append(nomes[0][0] + nomes[2] + dom)
    emails.append(nomes[0][0] + nomes[1] + nomes[2] + dom)
    return emails

def verificaMatricula(matricula):
    for aluno in dadosAlunos.alunos:
        if aluno.matricula == matricula:
            return aluno
    return False

# Lendo os dados da tabela CSV
dadosAlunos = Dados("./dados/alunos.csv")
dadosAlunos.lerDados()

# Requisitando a matricula do aluno
matricula = input("Digite sua matricula:")

# Buscando o aluno da matricula digitada
alunoLogado = verificaMatricula(matricula)

# Propondo os emails se logado, se não envia mensagem de erro
nomeAluno = alunoLogado.nome
emails = geraEmails(nomeAluno)
sinal = False

if alunoLogado:
    if(alunoLogado.status == "Ativo"):
        if(alunoLogado.uffmail == ""):
            print(nomeAluno.split()[0] + ", por favor escolha uma das opções abaixo para o seu UFFMail")
            
            sinal = True
            num = 1

            for email in emails:
                print(str(num) + " - " + email.lower())
                num += 1
        else:
            print("Vocês já possui um UFFemail, não é possível criar outro")
    else:
        print("Sua matrícula não está ativa")
else:
    print("Matrícula não cadastrada")


if(sinal == True):
    # Selecionando email desejado e atualizando a tabela
    numero = int(input())
    if(0 < numero < 6):
        index = numero - 1
        alunoLogado.setUffmail(emails[index].lower())
        dadosAlunos.attUffmail(alunoLogado)

        # Exibindo mensagem final
        print("A criação de seu e-mail (" + alunoLogado.uffmail + ") será feita nos próximos minutos.\nUm SMS foi enviado para " + alunoLogado.telefone + " com a sua senha de acesso.")
    else:
        print("Email não existente")
        

    