import database

from typing import List, Dict
from input import input_int, input_float

funcionarios: List[Dict] = []

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
    
    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "contrato": contrato_map[contrato_op],
        "valor_hora": valorPorHora,
        "horas_semanais": horasSemanais,
        "salario_mensal": salario
        }
    funcionarios.append(funcionario)
    database.salvar_funcionario(funcionario)
    
    print(f"Salário mensal calculado: R${salario:.2f}\n")
    print("Funcionário cadastrado com sucesso!\n")
    
def listar_funcionarios():
    print("\nFuncionários cadastrados:")
    for i in range(len(funcionarios)):
        print(f"Funcionário {i+1}: {funcionarios[i]['nome']}, Cargo: {funcionarios[i]['cargo']} salario: {funcionarios[i]['salario_mensal']}, Valor por hora: {funcionarios[i]['valor_hora']}, Horas trabalhadas: {funcionarios[i]['horas_semanais']}")
        print()