from typing import List, Dict
from applications.input import input_int

def menu_sub(titulo: str, opcoes: List[str]) -> int:
    print(f"\n{titulo}\n")
    for numero, opcao in enumerate(opcoes, 1):
        print(f"{numero}) {opcao}")
    try:
        return input_int("-> ")
    except ValueError:
        return 0