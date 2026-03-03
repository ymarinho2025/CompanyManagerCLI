import applications.database as database

from typing import List, Dict
from applications.funcionarios import funcionarios, listar_funcionarios
from applications.input import input_int

tarefas: List[Dict] = []

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
    tarefa = {"funcionario": nome_funcionario, "descricao": task}
    tarefas.append(tarefa)
    database.salvar_tarefa(tarefa)
    
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
        
        database.remover_tarefa_por_index(numero_tarefa)
        
        print(f"Tarefa de {rem['funcionario']} removida com sucesso!\n")
    else:
        print("Índice inválido.\n")