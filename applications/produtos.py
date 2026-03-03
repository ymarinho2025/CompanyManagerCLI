import database

from typing import List, Dict
from input import input_int, input_float

produtos: List[Dict] = []

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
    produto = {
        "nome": nome,
        "descricao": descricao,
        "preco_original": valor,
        "desconto_pct": desconto,
        "preco_final": round(valorComDesconto, 2)
        }
    produtos.append(produto)
    database.salvar_produto(produto)
    
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
        
        database.excluir_produto_por_nome(removido["nome"])
        
        print(f"Produto '{removido['nome']}' excluído com sucesso!\n")
    else:
        print("Índice inválido.\n")