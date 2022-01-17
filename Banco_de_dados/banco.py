import csv 

global banco_contatos
banco_contatos = []

# Criar o arquivo (caso não exista)
dados = open("Banco_de_dados/dados_agenda.csv","a+") #esse "a" é de apend e cria caso não existir esse arquivo
dados.close()

# Ler o arquivo
dados = open("Banco_de_dados/dados_agenda.csv","r+")
banco_contatos = dados.readlines()
dados.close()
lista_pessoas=[]

# FUNÇÃO SALVAR
def salvar():
    dados.close()
    print("\nAGENDA SALVA COM SUCESSO!")
    return None


# DIZER QUANTOS CONTATOS ESTÃO CADASTRADOS - OK
def quant_contatos():
    dados = open("Banco_de_dados/dados_agenda.csv","r+")
    banco_contatos = dados.readlines()
    dados.close()
    quant = len(banco_contatos)
    return quant
#print(quant_contatos())

# VERIFICAR CPF - OK
def verificar_chave(chave): #deve funcionar para cpf ou email
    banco_zerado = quant_contatos()
    if banco_zerado == 0:
        print("Por enquanto, o banco está vazio")
        cont = 0
    else:
        dados = open("Banco_de_dados/dados_agenda.csv","r+")
        banco_contatos = dados.readlines()
        #print(banco_contatos)
        for contato in banco_contatos:
            pessoa = contato.replace("\n","")
            lista = pessoa.split(";")
            x = chave in lista
            #print(chave in lista)
            if x == True:
                cont = 1
                break #para sair do laço
            else:
                cont = 0
    return cont
#teste = input("Qual CPF deseja verficar? ")
#print(verificar_chave(teste))

# INSIRIR CONTATO - OK
def inserir_contato():
    cpf = input("Digite o CPF: ")
    igual = verificar_chave(cpf)
    if igual == 1:
        print("Esse CPF já existe!")   
    else:
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")
        curso = input("Digite o curso: ")
        data_nasc = input("Digite a data de nascimento: ")
        lista_pessoas = [cpf, nome, sobrenome, email, telefone, curso, data_nasc]
        #print(lista_pessoas)
        dados = open("Banco_de_dados/dados_agenda.csv","a")
        writer = csv.writer(dados, delimiter=";",lineterminator="\n")
        #quoting = csv.QUOTE_ALL isso aqui é para colocar em aspas
        writer.writerow(lista_pessoas)
        salvar()
    return None
#inserir_contato()

# MOSTRAR LISTA - OK
def mostrar_lista():
    dados = open("Banco_de_dados/dados_agenda.csv","r+")
    banco_contatos = dados.readlines()
    #print(banco_contatos)
    dados.close()
    print("------ LISTA DE CONTATOS -----")
    for contato in banco_contatos:
        pessoa = contato.replace("\n","")
        lista = pessoa.split(";")
        print(f"CPF: {lista[0]}, nome: {lista[1]}, sobrenome: {lista[2]}, email: {lista[3]}, telefone: {lista[4]}, curso: {lista[5]}, data de nascimento: {lista[6]}")
    return None
#mostrar_lista()

# BUSCAR PARÂMETRO - OK
def buscar_contato(): #cpf, email, nome, curso
    chave = input("Digite a chave que deseja pesquisar: ")
    dados = open("Banco_de_dados/dados_agenda.csv","r+")
    banco_contatos = dados.readlines()
    existe = 0
    for contato in banco_contatos:
        pessoa = contato.replace("\n","")
        lista = pessoa.split(";")
        x = chave in lista
        if x == True:
            print("DADOS DO CONTATO:")
            print(f"CPF: {lista[0]}, nome: {lista[1]}, sobrenome: {lista[2]}, email: {lista[3]}, telefone: {lista[4]}, curso: {lista[5]}, data de nascimento: {lista[6]}")
            existe = 1
    dados.close()
    return existe
#buscar_contato()

def remover_contato(chave): #para cpf e email
    existe = verificar_chave(chave)
    #print(existe)
    if existe == 1:
        dados = open("Banco_de_dados/dados_agenda.csv","r")
        reader = csv.reader(dados,delimiter=';') #analisa o arquivo como csv
        data = list(reader) #armazena o conteúdo do arquivo na memória
        
        file = open("Banco_de_dados/dados_agenda.csv","w")
        writer = csv.writer(file, delimiter=';', lineterminator='\n') # Cria o objeto de escrita CSV:
        
        for contato in data:
            #pessoa = contato.replace("\n","")
            #lista = pessoa.split(";")
            x = chave in contato
            #print(chave in lista)
            if x != True:
                # Verifica se a linha não é uma avaliação do crítico:
                # Sim, então mantém a linha no arquivo:
                #print("entrou")
                writer.writerow(contato)
    else:
        print("Esse contato não existe!")
    return None
#chave = input("Digite o CPF que você quer remover: ")
#remover_contato(chave)

def atualizar():
    cpf = input("Digite o CPF que você deseja atualizar: ")
    existe = verificar_chave(cpf)
    if existe == 1:
        remover_contato(cpf)
    else:
        print("Esse contato ainda não existe.")
    inserir_contato()
    return None
#atualizar()





""" # função antiga
def verificar_chave(chave): #deve funcionar para cpf ou email
    print(type(chave))
    dados = open("Banco_de_dados/dados_agenda.csv","r+")
    banco_contatos = dados.readlines()
    #print(banco_contatos)
    for contato in banco_contatos:
        pessoa = contato.replace("\n","")
        lista = pessoa.split(";")
        print(lista[0])
        print(type(lista[0]))
        if lista[0] == chave:
            cont = 1
        else:
            cont = 0
    dados.close()
    return cont
"""