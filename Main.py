from typing import List, Dict

funcionarios: List[Dict] = []
clientes: List[Dict] = []
produtos: List[Dict] = []
tarefas: List[Dict] = []

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número válido.")

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite um número válido.")
            
def menu_principal() -> int:
    print("Sistema Marinho's Company (ADMIN)\n")
    print("Selecione uma opção:")
    print("1) Menu Funcionários")
    print("2) Menu Clientes")
    print("3) Produtos")
    print("4) RH")
    print("5) Sair")
    try:
        return input_int("-> ")
    except ValueError:
        return 0

def menu_sub(titulo: str, opcoes: List[str]) -> int:
    print(f"\n{titulo}\n")
    for numero, opcao in enumerate(opcoes, 1):
        print(f"{numero}) {opcao}")
    try:
        return input_int("-> ")
    except ValueError:
        return 0

def cadastrar_funcionario():
    nome = str(input("Digite o nome do funcionário: "))
    cargo = str(input("Digite o cargo do funcionário: "))
    contrato_op = input_int("1) PJ\n2) CLT\n-> ")
    contrato_map = {1: "PJ", 2: "CLT"}
    valorPorHora = input_float("Digite o valor por hora do funcionário: ")
    horasSemanais = input_float("Digite a Jornada semanal (ex: 44h semanais): ")
    print()
    
    semanas_mes = 4.33
    salario = valorPorHora * horasSemanais * semanas_mes
    
    if contrato_op == 1:  # PJ não tem descontos
        salario = salario 
    
    elif contrato_op == 2:
        if salario < 1412:
            salario = 1412  - (salario * 7.5 / 100)  # Salário mínimo CLT com desconto de INSS
            
        elif salario > 1412 and salario < 2666:
            salario = salario - (salario * 9 / 100)
            
        elif salario > 2666 and salario < 4000:
            salario = salario - (salario * 12 / 100)
            
        elif salario > 4000:
            salario = salario - (salario * 14 / 100) 
            
    else:
        print("Opção de contrato inválida. Cadastrando como CLT por padrão.")
        contrato_op = 2
    
    funcionarios.append({
        "nome": nome,
        "cargo": cargo,
        "contrato": contrato_map[contrato_op],
        "valor_hora": valorPorHora,
        "horas_semanais": horasSemanais,
        "salario_mensal": salario
    })
    
    print(f"Salário mensal calculado: R${salario:.2f}\n")
    print("Funcionário cadastrado com sucesso!\n")
    
def listar_funcionarios():
    print("\nFuncionários cadastrados:")
    for i in range(len(funcionarios)):
        print(f"Funcionário {i+1}: {funcionarios[i]['nome']}, Cargo: {funcionarios[i]['cargo']} salario: {funcionarios[i]['salario_mensal']}, Valor por hora: {funcionarios[i]['valor_hora']}, Horas trabalhadas: {funcionarios[i]['horas_semanais']}")
        print()
    
def cadastrar_cliente():
    nome = str(input("Digite o nome do cliente: "))
    idade = input_int("Digite a idade do cliente: ")
    print("Digite o gênero do cliente:")
    genero_op = input_int("1) Masculino\n2) Feminino\n3) Doente Mental\n-> ")
    genero_map = {1: "Masculino", 2: "Feminino", 3: "Doente Mental"}
    cliente_vip = ""
    while cliente_vip not in ('s','n'):
        cliente_vip = input("Cliente VIP (s/n): ").strip().lower()
        if cliente_vip not in ('s','n'):
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

            
    clientes.append({
        "nome": nome,
        "idade": idade,
        "genero": genero_map[genero_op],
        "vip": cliente_vip == "s"
        })
    print("Cliente cadastrado com sucesso!\n")
            
def listar_clientes():
    print("\nClientes cadastrados:")
    for i in range(len(clientes)):
        print(f"Cliente {i+1}: {clientes[i]['nome']}, Idade: {clientes[i]['idade']}, Gênero: {clientes[i]['genero']}, VIP: {clientes[i]['vip']}")
        print()
        
def cadastrar_produto():
    nome = str(input("Digite o nome do produto: "))
    descricao = str(input("Digite a descrição do produto: "))
    valor = input_float("Preço (R$): ")
    print("Digite o desconto do produto:")
    desconto = input_float("Desconto (%) (ex: 10 para 10%): ")
    if desconto > 100:
        print("Desconto não pode ser maior que 100%. Ajustando para 100%.")
        desconto = 100.0
    valorComDesconto = valor - (valor * (desconto / 100))
    produtos.append({
        "nome": nome,
        "descricao": descricao,
        "preco_original": valor,
        "desconto_pct": desconto,
        "preco_final": round(valorComDesconto, 2)
    })
    print("Produto cadastrado com sucesso!\n")
    
def listar_produtos():
    print("\nProdutos cadastrados:")
    for i in range(len(produtos)):
        print(f"Produto {i+1}: {produtos[i]['nome']}, Descrição: {produtos[i]['descricao']}, Preço Original: R${produtos[i]['preco_original']:.2f}, Desconto: {produtos[i]['desconto_pct']}%, Preço Final: R${produtos[i]['preco_final']:.2f}")
        print()
        
def excluir_produtos():
    if not produtos:
        print("Nenhum produto cadastrado para excluir.\n")
        return
    listar_produtos()
    numero_produto = input_int("Digite o numero do produto a ser excluído: ")
    if numero_produto == 0:
        print("Cancelado.\n")
        return
    if 1 <= int(numero_produto) <= len(produtos):
        removido = produtos.pop(int(numero_produto) - 1)
        print(f"Produto '{removido['nome']}' excluído com sucesso!\n")
    else:
        print("Índice inválido.\n")
        
def enviar_tarefa():
    if not funcionarios:
        print("Nenhum funcionário cadastrado para enviar tarefas.\n")
        return
    listar_funcionarios()
    nome_funcionario = input("Digite o nome do funcionário para enviar a tarefa: ")
    nomes = [f["nome"] for f in funcionarios]
    if nome_funcionario not in nomes:
        print("Funcionário não encontrado. Tente novamente.\n")
        return
    task = input("Digite a tarefa a ser realizada: ")
    tarefas.append({
        "funcionario": nome_funcionario,
        "descricao": task
        })
    for i, t in enumerate(tarefas, 1):
        print(f"Tarefa {i}: Funcionário: {t['funcionario']}, Tarefa: {t['descricao']}")
        print()
    
def listar_tarefas():
    print("\nTarefas atuais:")
    for i in range(len(tarefas)):
        print(f"Tarefa {i+1}: Funcionário: {tarefas[i]['funcionario']}, Tarefa: {tarefas[i]['descricao']}")
        print()
        
def remover_tarefas():
    if not tarefas:
        print("Nenhuma tarefa para remover.\n")
        return
    listar_tarefas()
    numero_tarefa = input_int("Digite o número da tarefa para remover (0 para cancelar):: ")
    if numero_tarefa == 0:
        print("Cancelado.\n")
        return
    if 1 <= numero_tarefa <= len(tarefas):
        rem = tarefas.pop(numero_tarefa - 1)
        print(f"Tarefa de {rem['funcionario']} removida com sucesso!\n")
    else:
        print("Índice inválido.\n")
        
def main():
    while True:
        main_choice = menu_principal()
        print()
        if main_choice == 1:
            while True:
                sub = menu_sub("Menu Funcionários", ["Cadastrar Funcionário", "Listar Funcionários", "Voltar"])
                print()
                if sub == 1:
                    cadastrar_funcionario()
                elif sub == 2:
                    listar_funcionarios()
                elif sub == 3:
                    break
                else:
                    print("Opção inválida.\n")

        elif main_choice == 2:
            while True:
                sub = menu_sub("Menu Clientes", ["Cadastrar Cliente", "Listar Clientes", "Voltar"])
                print()
                if sub == 1:
                    cadastrar_cliente()
                elif sub == 2:
                    listar_clientes()
                elif sub == 3:
                    break
                else:
                    print("Opção inválida.\n")

        elif main_choice == 3:
            while True:
                sub = menu_sub("Produtos", ["Cadastrar Produto", "Listar Produtos", "Excluir Produto", "Voltar"])
                print()
                if sub == 1:
                    cadastrar_produto()
                elif sub == 2:
                    listar_produtos()
                elif sub == 3:
                    excluir_produtos()
                elif sub == 4:
                    break
                else:
                    print("Opção inválida.\n")

        elif main_choice == 4:
            while True:
                sub = menu_sub("RH - Tarefas", ["Enviar tarefa para funcionário", "Tarefas atuais", "Remover Tarefas", "Voltar"])
                print()
                if sub == 1:
                    enviar_tarefa()
                elif sub == 2:
                    listar_tarefas()
                elif sub == 3:
                    remover_tarefas()
                elif sub == 4:
                    break
                else:
                    print("Opção inválida.\n")

        elif main_choice == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida no menu principal.\n")

if __name__ == "__main__":
    main()