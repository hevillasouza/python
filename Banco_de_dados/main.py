import menu
import banco

while True:
    escolha = menu.escolha_usuario()

    if escolha == 1:
        # Opção 1. Inserir contato
        print("\n\t - Iniciando o processo de inserir um contato -\n")
        banco.inserir_contato()
        print()
    elif escolha == 2:
        # Opção 2. Atualizar contato
        print("\n\t - Iniciando o processo de atualizar um contato -\n")
        banco.atualizar()
        print()
    elif escolha == 3:
        # Opção 3. Mostrar agenda
        print("\n\t - Iniciando o processo de mostrar os contatos -\n")
        banco.mostrar_lista()
        print()
    elif escolha == 4:
        # Opção 4. Buscar contato pelo CPF
        print("\n\t - Iniciando o processo de buscar o contato pelo CPF-\n")
        existe = banco.buscar_contato()
        if existe == 0:
            print("Esse contato não existe!")
        print()
    elif escolha == 5:
        # Opção 5. Buscar contato pelo email
        print("\n\t - Iniciando o processo de buscar o contato pelo email-\n")
        existe = banco.buscar_contato()
        if existe == 0:
            print("Esse contato não existe!")
        print()
    elif escolha == 6:
        # Opção 6. Buscar contato pelo nome
        print("\n\t - Iniciando o processo de buscar o contato pelo nome-\n")
        existe = banco.buscar_contato()
        if existe == 0:
            print("Esse contato não existe!")
        print()
    elif escolha == 7:
        # Opção 7. Buscar contato pelo curso
        print("\n\t - Iniciando o processo de buscar o contato pelo curso-\n")
        existe = banco.buscar_contato()
        if existe == 0:
            print("Esse contato não existe!")
        print()
    elif escolha == 8:
        # Opção 8. Quantidade de contatos
        print("\n\t - Iniciando o processo de contagem da quantidade de contatos -\n")
        quant = banco.quant_contatos()
        print(f"A agenda conta com {quant} contatos!\n")
    elif escolha == 9:
        # Opção 9. Deletar contato pelo CPF
        print("\n\t - Iniciando o processo de remover um contato pelo CPF -\n")
        chave = input("Digite o CPF do contato que você quer remover: ")
        banco.remover_contato(chave)
        print()
    elif escolha == 10:
        # Opção 10. Deletar contato pelo email
        print("\n\t - Iniciando o processo de remover um contato pelo email -\n")
        chave = input("Digite o email do contato que você quer remover: ")
        banco.remover_contato(chave)
        print()
    elif escolha == 11:
        # Opção 11. Salvar e sair
        banco.salvar()
        break
    else:
        print("Operação inválida!\nTente novamente!\n")


