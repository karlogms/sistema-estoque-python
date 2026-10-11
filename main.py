print("======= SISTEMA DE ESTOQUE ======")
print("1 - Cadastrar Produto")
print("2 - Listar Produtos")
print("3 - Buscar Produtos")
print("4 - Atualizar Estoque")
print("5 - Excluir Produto")
print("0 - Sair")

opcao = input ("Escolha uma opção: ")
print("Você escolheu a opção: ", opcao)


if opcao == "1":
    print("Você escolheu cadastrar produto")

elif opcao == "2":
    print("Você escolheu listar os produtos")

elif opcao == "3":
    print ("Você escolheu buscar um produto")

elif opcao == "4":
    print("Você escolheu atualizar o estoque")

elif opcao == "5":
    print("Você escolheu excluir um produto")

elif opcao == "0":
    print("Saindo do sistema...")



produtos = []

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade em estoque: "))

produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

produtos.append(produto)
print("Produto cadastrado com sucesso!")
