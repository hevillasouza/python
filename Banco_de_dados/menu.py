def escolha_usuario():
    print("""----------AGENDA DE CONTATOS----------
        Opções:
            1. Inserir contato;
            2. Atualizar contato;
            3. Mostrar agenda;
            4. Buscar contato pelo CPF;
            5. Buscar contato pelo email;
            6. Buscar contato pelo nome;
            7. Buscar contato pelo curso;
            8. Quantidade de contatos;
            9. Deletar contato pelo CPF;
            10. Deletar contato pelo email;
            11. Salvar e sair.""")
    opcao = int(input("Digite sua opção: "))
    return opcao

