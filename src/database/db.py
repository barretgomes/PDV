"""
Gerenciador de banco de dados do sistema de PDV
"""

import sqlite3
import os
from pathlib import Path


class Database:
    """Classe para gerenciar o banco de dados SQLite"""

    def __init__(self, db_name="pdv.db"):
        """Inicializa a conexão com o banco de dados"""
        # Define o caminho do banco de dados
        self.db_path = Path(__file__).parent.parent.parent / db_name
        self.connection = None
        self.create_connection()
        self.create_tables()

    def create_connection(self):
        """Cria conexão com o banco de dados"""
        try:
            self.connection = sqlite3.connect(str(self.db_path))
            print(f"✅ Conectado ao banco de dados: {self.db_path}")
        except sqlite3.Error as e:
            print(f"❌ Erro ao conectar ao banco de dados: {e}")

    def create_tables(self):
        """Cria as tabelas do banco de dados"""
        if self.connection is None:
            return

        cursor = self.connection.cursor()

        # Tabela de Clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE,
                email TEXT,
                telefone TEXT,
                endereco TEXT,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Tabela de Produtos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL DEFAULT 0,
                categoria TEXT,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Tabela de Vendas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER,
                data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total REAL NOT NULL,
                forma_pagamento TEXT,
                FOREIGN KEY (cliente_id) REFERENCES clientes (id)
            )
        ''')

        # Tabela de Itens de Venda
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens_venda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                venda_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL,
                subtotal REAL NOT NULL,
                FOREIGN KEY (venda_id) REFERENCES vendas (id),
                FOREIGN KEY (produto_id) REFERENCES produtos (id)
            )
        ''')

        self.connection.commit()
        print("✅ Tabelas criadas com sucesso!")

    def close_connection(self):
        """Fecha a conexão com o banco de dados"""
        if self.connection:
            self.connection.close()
            print("✅ Conexão com banco de dados fechada")


# Exemplo de uso
if __name__ == "__main__":
    db = Database()
    db.close_connection()
