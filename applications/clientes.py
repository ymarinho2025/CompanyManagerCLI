import database

from typing import List, Dict
from input import input_int

clientes: List[Dict] = []

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

            
            cliente = {
                "nome": nome,
                "idade": idade,
                "genero": genero_map[genero_op],
                "vip": cliente_vip == "s"}
            clientes.append(cliente)
            database.salvar_cliente(cliente)
            
            print("Cliente cadastrado com sucesso!\n")
            
def listar_clientes():
    print("\nClientes cadastrados:")
    for i in range(len(clientes)):
        print(f"Cliente {i+1}: {clientes[i]['nome']}, Idade: {clientes[i]['idade']}, Gênero: {clientes[i]['genero']}, VIP: {clientes[i]['vip']}")
        print()