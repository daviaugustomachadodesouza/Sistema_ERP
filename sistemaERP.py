# listas RH
funcionarios_nomes = []
funcionarios_cargos = []
funcionarios_salarios = []

# lista estoque
estoque_produtos = []
estoque_quantidades = []
estoque_precos = []

# chamados TI
chamados_titulos = []
chamados_status = []

sistema_ativo = True

while sistema_ativo == True:
    print("\nSISTEMA ERP - TELA INICIAL")
    print("MENU:")
    print("1-Modulo RH")
    print("2-Modulo Estoque")
    print("3-Modulo de chamados")
    print("4-Relatorios Gerais")
    print("5-Sair do sistema")

    escolha = input("Digite sua escolha de opcao:")

    if escolha == "5":
        print("Salvando seus dados...")
        sistema_ativo = False

    # parte do modulo RH
    elif escolha == "1":
        sistema_rh_ativo = True
        while sistema_rh_ativo == True:
            print("\n1-Cadastrar")
            print("2-Listar")
            print("3-Demitir")
            print("4-Voltar ao menu principal")

            escolha_rh = input("Digite sua escolha do Modulo RH:")
            if escolha_rh == "4":
                print("Saindo do modulo RH")
                sistema_rh_ativo = False
                break

            elif escolha_rh == "1":
                nome_novo = input("Digite o nome do funcionario: ")
                cargo_novo = input("Digite o cargo do funcionario: ")
                salario_novo = float(input("Digite o salario do funcionario: "))
                funcionarios_nomes = funcionarios_nomes + [nome_novo]
                funcionarios_cargos = funcionarios_cargos + [cargo_novo]
                funcionarios_salarios = funcionarios_salarios + [salario_novo]
                print("Funcionario cadastrado com sucesso!")

            elif escolha_rh == "2":
                indice = 0
                for nome_atual in funcionarios_nomes:
                    cargo_atual = funcionarios_cargos[indice]
                    salario_atual = funcionarios_salarios[indice]
                    print("ID:", indice, "|Nome:", nome_atual, "|Cargo:", cargo_atual)
                    indice = indice + 1

            elif escolha_rh == "3":
                indice = 0
                funcionario_demitido = input(
                    "Digite o nome do funcionario a ser demitido:"
                )
                novos_nomes = []
                novos_cargos = []
                novos_salarios = []
                for nome_atual in funcionarios_nomes:
                    if nome_atual == funcionario_demitido:
                        print("Funcionario demitido com sucesso!")
                    else:
                        novos_nomes = novos_nomes + [funcionarios_nomes[indice]]
                        novos_cargos = novos_cargos + [funcionarios_cargos[indice]]
                        novos_salarios = novos_salarios + []
                        funcionarios_salarios[indice]
                        print("Funcionario nao encontrado!")
                    indice + 1
                funcionarios_nomes = novos_nomes
                funcionarios_cargos = novos_cargos
                funcionarios_salarios = novos_salarios

    # parte do modulo de estoque
    elif escolha == "2":
        menu_estoque_ativo = True
        while menu_estoque_ativo == True:
            print("\n1-Adicionar produto")
            print("2-Listar estoque")
            print("3-Dar baixa(Vender)")
            print("4-Voltar ao menu principal")

            escolha_estoque = input("Digite sua escolha do modulo de estoque:")

            if escolha_estoque == "4":
                print("Salvando seus dados...")
                print("Voltando ao menu principal!")
                menu_estoque_ativo = False
                break

            elif escolha_estoque == "1":
                nome_produto = input("Digite o nome do seu produto:")
                quantidade_produto = int(input("Digite a quantas unidades do produto:"))
                preco_produto = float(input("Digite o preco do seu produto:"))
                estoque_produtos = estoque_produtos + [nome_produto]
                estoque_quantidades = estoque_quantidades + [quantidade_produto]
                estoque_precos = estoque_precos + [preco_produto]
                print("Produto(s) adicionados com sucesso!")

            elif escolha_estoque == "2":
                indice = 0
                for produto in estoque_produtos:
                    quantidade = estoque_quantidades[indice]
                    preco = estoque_precos[indice]
                    print(
                        "Produto:",
                        produto,
                        "|Quantidade:",
                        quantidade,
                        "|Preco R$:",
                        preco,
                    )
                    indice = indice + 1

            elif escolha_estoque == "3":
                produto_procurado = input("Digite o nome do produto:")
                indice_atual = 0
                indice_encontrado = -1
                for produto in estoque_produtos:
                    if produto == produto_procurado:
                        indice_encontrado = indice_atual
                    indice_atual = indice_atual + 1
                    if produto == -1:
                        print("Seu produto nao foi encontrado")
                    else:
                        qtd_vendas = int(input("Quantas unidades deseja vender?"))
                    if qtd_vendas <= estoque_quantidades[indice_encontrado]:
                        estoque_quantidades[indice_encontrado] = (
                            estoque_quantidades[indice_encontrado] - qtd_vendas
                        )
                        print("Venda realizada com sucesso!")
                    else:
                        print("Estoque insuficiente!")

    # parte modulo de chamado
    elif escolha == "3":
        menu_chamados_ativo = True
        while menu_chamados_ativo == True:
            print("\n1-Abrir chamado")
            print("2-Listar chamado")
            print("3-Resolver chamado")
            print("4-Voltar ao menu principal")
            escolha_chamados = input("Digite sua escolha do modulo de chamados:")
            titulo_problema = input("Digite seu problema para acionar um chamado:")

            if escolha_chamados == "4":
                menu_chamados_ativo = False
                print("Voltando ao menu principal!")

            elif escolha_chamados == "1":
                chamados_titulos = chamados_titulos + [titulo_problema]
                chamados_status = chamados_status + ["ABERTO!"]
                print(chamados_titulos)
                print(f"Chamado status foi {chamados_status}")
                print("Seu chamado foi processado!")

            elif escolha_chamados == "2":
                indice = 0
                for titulos in chamados_titulos:
                    status = chamados_status[indice]
                    print(f"O chamado '{titulos}' está com status: {status}")
                    indice = indice + 1

            elif escolha_chamados == "3":
                nome_busca = input("Qual nome do chamado que foi pedido?")
                indice_encontrado = -1
                indice = 0
                for titulo in chamados_titulos:
                    if titulo == nome_busca:
                        indice_encontrado = indice
                        break
                    indice = indice + 1
                if indice_encontrado != -1:
                    chamados_status[indice_encontrado] = "RESOLVIDO"
                    print("Chamado atualizado para RESOLVIDO!")
                else:
                    print("Problema nao encontrado.Verifique novamente!")

    #relatorios gerais
    elif escolha == "4":
        total_salario = 0
        maior_salario = 0
        maior_nome = ""
        indice = 0
        
        for salario_avaliado in funcionarios_salarios:
            total_salario = total_salario + salario_avaliado
            
            if salario_avaliado > maior_salario:
                maior_salario = salario_avaliado
                maior_nome = funcionarios_nomes[indice]
                
            indice = indice + 1
            
        print("Total da folha de pagamento R$:", total_salario)
        print("Maior salário R$:", maior_salario, "- Funcionário:", maior_nome)

        valor_total_empresa = 0
        indice_estoque = 0
        
        for produto in estoque_produtos:
            valor_deste_produto = estoque_quantidades[indice_estoque] * estoque_precos[indice_estoque]
            valor_total_empresa = valor_total_empresa + valor_deste_produto
            indice_estoque = indice_estoque + 1
            
        print("Valor total investido no estoque R$:", valor_total_empresa)

        chamados_abertos = 0
        chamdos_resolvidos = 0

        for status in chamados_status:
            if status == "ABERTO!":
                chamados_abertos = chamados_abertos + 1
            elif status == "RESOLVIDO!":
                chamdos_resolvidos = chamdos_resolvidos + 1
                
            print("quantidade de chamdos abertos:",chamados_abertos)
            print("quantidade de chamados resolvidos:",chamdos_resolvidos)