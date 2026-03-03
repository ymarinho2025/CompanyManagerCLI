# database.py
import sqlite3
from typing import List, Dict, Any

DB_NAME = "sistema.db"

def _conectar():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    return conn, cur

def init_db():
    conn, cur = _conectar()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        genero TEXT NOT NULL,
        vip INTEGER NOT NULL
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        contrato TEXT NOT NULL,
        valor_hora REAL,
        horas_semanais REAL,
        salario_mensal REAL
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco_original REAL NOT NULL,
        desconto_pct REAL NOT NULL,
        preco_final REAL NOT NULL
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        funcionario TEXT NOT NULL,
        descricao TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()

# --- CLIENTES ---
def carregar_clientes() -> List[Dict[str, Any]]:
    conn, cur = _conectar()
    rows = cur.execute("SELECT nome, idade, genero, vip FROM clientes ORDER BY id;").fetchall()
    conn.close()
    return [
        {"nome": nome, "idade": idade, "genero": genero, "vip": bool(vip)}
        for nome, idade, genero, vip in rows
    ]

def salvar_cliente(cliente: Dict[str, Any]) -> None:
    conn, cur = _conectar()
    cur.execute(
        "INSERT INTO clientes (nome, idade, genero, vip) VALUES (?, ?, ?, ?);",
        (cliente["nome"], cliente["idade"], cliente["genero"], 1 if cliente["vip"] else 0)
    )
    conn.commit()
    conn.close()

# --- FUNCIONÁRIOS ---
def carregar_funcionarios() -> List[Dict[str, Any]]:
    conn, cur = _conectar()
    rows = cur.execute(
        "SELECT nome, cargo, contrato, valor_hora, horas_semanais, salario_mensal FROM funcionarios ORDER BY id;"
    ).fetchall()
    conn.close()
    return [
        {
            "nome": nome,
            "cargo": cargo,
            "contrato": contrato,
            "valor_hora": valor_hora,
            "horas_semanais": horas_semanais,
            "salario_mensal": salario_mensal
        }
        for nome, cargo, contrato, valor_hora, horas_semanais, salario_mensal in rows
    ]

def salvar_funcionario(funcionario: Dict[str, Any]) -> None:
    conn, cur = _conectar()
    cur.execute("""
        INSERT INTO funcionarios
        (nome, cargo, contrato, valor_hora, horas_semanais, salario_mensal)
        VALUES (?, ?, ?, ?, ?, ?);
    """, (
        funcionario["nome"],
        funcionario["cargo"],
        funcionario["contrato"],
        funcionario.get("valor_hora", None),
        funcionario.get("horas_semanais", None),
        funcionario.get("salario_mensal", None)
    ))
    conn.commit()
    conn.close()

# --- PRODUTOS ---
def carregar_produtos() -> List[Dict[str, Any]]:
    conn, cur = _conectar()
    rows = cur.execute(
        "SELECT nome, descricao, preco_original, desconto_pct, preco_final FROM produtos ORDER BY id;"
    ).fetchall()
    conn.close()
    return [
        {
            "nome": nome,
            "descricao": descricao,
            "preco_original": preco_original,
            "desconto_pct": desconto_pct,
            "preco_final": preco_final
        }
        for nome, descricao, preco_original, desconto_pct, preco_final in rows
    ]

def salvar_produto(produto: Dict[str, Any]) -> None:
    conn, cur = _conectar()
    cur.execute("""
        INSERT INTO produtos (nome, descricao, preco_original, desconto_pct, preco_final)
        VALUES (?, ?, ?, ?, ?);
    """, (
        produto["nome"],
        produto.get("descricao", ""),
        produto["preco_original"],
        produto["desconto_pct"],
        produto["preco_final"]
    ))
    conn.commit()
    conn.close()

def excluir_produto_por_nome(nome: str) -> None:
    conn, cur = _conectar()
    cur.execute("DELETE FROM produtos WHERE nome = ?;", (nome,))
    conn.commit()
    conn.close()

# --- TAREFAS ---
def carregar_tarefas() -> List[Dict[str, Any]]:
    conn, cur = _conectar()
    rows = cur.execute("SELECT funcionario, descricao FROM tarefas ORDER BY id;").fetchall()
    conn.close()
    return [{"funcionario": f, "descricao": d} for f, d in rows]

def salvar_tarefa(tarefa: Dict[str, Any]) -> None:
    conn, cur = _conectar()
    cur.execute("INSERT INTO tarefas (funcionario, descricao) VALUES (?, ?);", (tarefa["funcionario"], tarefa["descricao"]))
    conn.commit()
    conn.close()

def remover_tarefa_por_index(index: int) -> None:
    conn, cur = _conectar()
    # index assumed 1-based matching UI order; delete by id needs different approach.
    # For simplicity, remove by selecting id at that offset.
    rows = cur.execute("SELECT id FROM tarefas ORDER BY id;").fetchall()
    if 1 <= index <= len(rows):
        row_id = rows[index - 1][0]
        cur.execute("DELETE FROM tarefas WHERE id = ?;", (row_id,))
        conn.commit()
    conn.close()