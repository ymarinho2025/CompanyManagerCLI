from typing import List, Dict
import applications.funcionarios as func
from applications.funcionarios import funcionarios, cadastrar_funcionario, listar_funcionarios
from applications.clientes import clientes, cadastrar_cliente, listar_clientes
from applications.produtos import produtos, cadastrar_produto, listar_produtos, excluir_produtos
from applications.tarefas import tarefas, enviar_tarefa, listar_tarefas, remover_tarefas
from applications.input import input_int
from applications.submenu import menu_sub
            
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