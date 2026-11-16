
produtos = []

while True:
    print("\n======= SISTEMA DE ESTOQUE ======")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produtos")
    print("4 - Atualizar Estoque")
    print("5 - Excluir Produto")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # CADASTRAR PRODUTO
    if opcao == "1":
        print("\n======= CADASTRAR PRODUTO ======")

        nome = input("Digite o nome do produto: ").strip()

        if nome == "":
            print("O nome do produto não pode ficar vazio!")
            continue

        try:
            preco = float(input("Digite o preço do produto: ").replace(",", "."))
            quantidade = int(input("Digite a quantidade em estoque: "))

            if preco < 0 or quantidade < 0:
                print("Preço e quantidade não podem ser negativos!")
                continue

        except ValueError:
            print("Digite um preço e uma quantidade válidos!")
            continue

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)

        print("Produto cadastrado com sucesso!")

    # LISTAR PRODUTOS
    elif opcao == "2":
        print("\n======= PRODUTOS CADASTRADOS ======")

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print("--------------------------")
                print("Nome:", produto["nome"])
                print("Preço: R$", produto["preco"])
                print("Quantidade:", produto["quantidade"])

            print("--------------------------")

    # BUSCAR PRODUTO
    elif opcao == "3":
        print("\n======= BUSCAR PRODUTO ======")

        nome_busca = input("Digite o nome do produto: ").strip()

        encontrou = False

        for produto in produtos:
            if produto["nome"].lower() == nome_busca.lower():
                print("\nProduto encontrado!")
                print("Nome:", produto["nome"])
                print("Preço: R$", produto["preco"])
                print("Quantidade:", produto["quantidade"])

                encontrou = True

        if encontrou == False:
            print("Produto não encontrado!")

    # ATUALIZAR ESTOQUE
    elif opcao == "4":
        print("\n======= ATUALIZAR ESTOQUE ======")

        nome_busca = input("Digite o nome do produto: ").strip()

        encontrou = False

        for produto in produtos:
            if produto["nome"].lower() == nome_busca.lower():

                print("\nProduto encontrado!")
                print("Quantidade atual:", produto["quantidade"])

                try:
                    nova_quantidade = int(input("Digite a nova quantidade: "))

                    if nova_quantidade < 0:
                        print("A quantidade não pode ser negativa!")
                        encontrou = True
                        break

                    produto["quantidade"] = nova_quantidade

                    print("Estoque atualizado com sucesso!")

                except ValueError:
                    print("Digite uma quantidade válida!")

                encontrou = True
                break

        if encontrou == False:
            print("Produto não encontrado!")

    # EXCLUIR PRODUTO
    elif opcao == "5":
        print("\n======= EXCLUIR PRODUTO ======")

        nome_busca = input("Digite o nome do produto: ").strip()

        encontrou = False

        for produto in produtos:
            if produto["nome"].lower() == nome_busca.lower():

                print("\nProduto encontrado:", produto["nome"])

                confirmacao = input("Deseja realmente excluir? (s/n): ").lower()

                if confirmacao == "s":
                    produtos.remove(produto)
                    print("Produto excluído com sucesso!")
                else:
                    print("Exclusão cancelada.")

                encontrou = True
                break

        if encontrou == False:
            print("Produto não encontrado!")

    # SAIR DO SISTEMA
    elif opcao == "0":
        print("Saindo do sistema...")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida! Escolha uma opção de 0 a 5.")
