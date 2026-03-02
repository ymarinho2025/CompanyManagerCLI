funcionarios = []
clientes = []
produtos = []
tarefas = []
while True:
    print("Sistema Marinho's Company (ADMIN)\n")
    print("Selecione uma opção:")
    choice1 = int(input("1) Menu Funcionarios\n2) Menu Clientes\n3) Produtos\n4) RH\n5) Sair\n-> "))
    print()
    
    if choice1 == 1:
        while True:
            
            choice1 = int(input("1) Cadastrar Funcionário\n2) Listar Funcionários\n3) Sair\n-> "))
            print()
            
            if choice1 == 1:
                
                nome = str(input("Digite o nome do funcionário: "))
                cargo = str(input("Digite o cargo do funcionário: "))
                valorPorHora = float(input("Digite o valor por hora do funcionário: "))
                horasTrabalhadas = float(input("Digite as horas trabalhadas do funcionário: "))
                salario_base = float(input("Digite o salário base do funcionário: "))
                funcionarios.append((nome, cargo, valorPorHora, horasTrabalhadas, salario_base))
                
                print("Funcionário cadastrado com sucesso!\n")
                
            
            elif choice1 == 2:
                
                print("\nFuncionários cadastrados:")
                for i in range(len(funcionarios)):
                    print(f"Funcionário {i+1}: {funcionarios[i][0]}, Cargo: {funcionarios[i][1]} salario base: {funcionarios[i][4]}, Valor por hora: {funcionarios[i][2]}, Horas trabalhadas: {funcionarios[i][3]}")
                    print()
            
            elif choice1 == 3:
                break
            
    elif choice1 == 2:
        while True:
            
            choice1 = int(input("1) Cadastrar Cliente\n2) Listar Clientes\n3) Sair\n-> "))
            print()
            
            if choice1 == 1:
                
                nome = str(input("Digite o nome do cliente: "))
                idade = int(input("Digite a idade do cliente: "))
                print("Digite o gênero do cliente:")
                genero = int(input("1) Masculino\n2) Feminino\n3) Doente Mental\n-> "))
                while True:
                    cliente_vip = str(input("Cliente VIP (s/n): ")).lower()
                    while cliente_vip not in ('s','n'):
                        print("Opção inválida. Digite 's' para sim ou 'n' para não.")
                    if cliente_vip in ('s','n'):
                        break
                clientes.append((nome, idade, genero, cliente_vip))
                
                print("Cliente cadastrado com sucesso!\n")
            
            elif choice1 == 2:
                
                print("\nClientes cadastrados:")
                for i in range(len(clientes)):
                    print(f"Cliente {i+1}: {clientes[i][0]}, Idade: {clientes[i][1]}, Gênero: {clientes[i][2]}, VIP: {clientes[i][3]}")
                    print()
                    
            elif choice1 == 3:
                break
            
    elif choice1 == 3:
        while True:
            
            choice1 = int(input("1) Cadastrar Produto\n2) Listar Produtos\n3) Excluir Produtos\n4) Sair\n-> "))
            print()
            
            if choice1 == 1:
                nome = str(input("Digite o nome do produto: "))
                descricao = str(input("Digite a descrição do produto: "))
                valor = float(input("Digite o valor do produto: "))
                print("Digite o desconto do produto:")
                desconto = float(input("Coloque o numero da porcentagem por exemplo (10) se for 10%\n-> "))
                valor = valor - (valor * (desconto / 100))
                produtos.append((nome, descricao, valor))
                
            elif choice1 == 2:
                
                print("\nProdutos cadastrados:")
                for i in range(len(produtos)):
                    print(f"Produto {i+1}: {produtos[i][0]}, Descrição: {produtos[i][1]}, Valor: {produtos[i][2]}, Desconto: {produtos[i][3]}")
                    print()
                    
            elif choice1 == 3:
                nome_produto = input("Digite o nome do produto a ser excluído: ")
                produtos = [produto for produto in produtos if produto[0] != nome_produto]
                print(f"Produto '{nome_produto}' excluído com sucesso!\n")
            
            elif choice1 == 4:
                break
                
    elif choice1 == 4:
        while True:
            choice1 = int(input("1) Enviar tarefa para funcionário\n2) Tarefas atuais\n3) Remover Tarefas\n4) Sair\n-> "))
            print()
            
            if choice1 == 1:
                
                print("\nFuncionários na empresa:")
                for i in range(len(funcionarios)):
                    print(f"Funcionário {i+1}: {funcionarios[i][0]}")
                    print()
                    
                nome_funcionario = input("Digite o nome do funcionário para enviar a tarefa: ")
                
                if nome_funcionario not in [funcionario[0] for funcionario in funcionarios]:
                    print("Funcionário não encontrado. Tente novamente.\n")
                    continue
                
                task = input("Digite a tarefa a ser realizada: ")
                
                tarefas.append((nome_funcionario, task))
                print(f"Tarefa '{task}' enviada para o funcionário '{nome_funcionario}' com sucesso!")
                print()
                 
            elif choice1 == 2:
                
                print("\nTarefas atuais:")
                for i in range(len(tarefas)):
                    print(f"Tarefa {i+1}: Funcionário: {tarefas[i][0]}, Tarefa: {tarefas[i][1]}")
                    print()
                    
            elif choice1 == 3:
                
                nome_funcionario = input("Digite o nome do funcionário para remover as tarefas: ")
                tarefas = [tarefa for tarefa in tarefas if tarefa[0] != nome_funcionario]
                print(f"Tarefas do funcionário '{nome_funcionario}' removidas com sucesso!\n")
            
            elif choice1 == 4:
                break
            
    elif choice1 == 5:
        break
            