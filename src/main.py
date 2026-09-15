"""
Arquivo principal do Sistema de PDV
Ponto de Venda (PDV) - Sistema de Vendas Completo
"""

import sys
import urllib.request
import urllib.error
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QTabWidget,
    QLineEdit, QMessageBox, QTextEdit
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from src.database.db import Database


def check_online_status(url: str = "https://github.com"):
    """Verifica se a URL fornecida está acessível."""
    try:
        request = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(request, timeout=10) as response:
            return {
                "online": response.status < 400,
                "status": f"online ({response.status})" if response.status < 400 else f"offline ({response.status})",
                "url": url,
            }
    except Exception as exc:
        return {
            "online": False,
            "status": f"offline ({type(exc).__name__})",
            "url": url,
        }


class PDVMainWindow(QMainWindow):
    """Janela principal do sistema de PDV"""

    def __init__(self):
        super().__init__()
        self.db = Database()
        self.setWindowTitle("Sistema de PDV - Ponto de Venda")
        self.setGeometry(100, 100, 1200, 700)
        self.initUI()

    def initUI(self):
        """Inicializa a interface gráfica"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QVBoxLayout()

        # Título
        title = QLabel("📊 Sistema de PDV - Ponto de Venda")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)

        # Abas do sistema
        tabs = QTabWidget()

        # Aba 1: Vendas
        vendas_widget = self.create_vendas_tab()
        tabs.addTab(vendas_widget, "💳 Vendas")

        # Aba 2: Estoque
        estoque_widget = self.create_estoque_tab()
        tabs.addTab(estoque_widget, "📦 Estoque")

        # Aba 3: Clientes
        clientes_widget = self.create_clientes_tab()
        tabs.addTab(clientes_widget, "👥 Clientes")

        # Aba 4: Relatórios
        relatorios_widget = self.create_relatorios_tab()
        tabs.addTab(relatorios_widget, "📈 Relatórios")

        # Aba 5: Status online
        status_widget = self.create_status_tab()
        tabs.addTab(status_widget, "🌐 Status Online")

        # Adicionar ao layout principal
        main_layout.addWidget(title)
        main_layout.addWidget(tabs)

        central_widget.setLayout(main_layout)

    def create_vendas_tab(self):
        """Cria a aba de Vendas"""
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("🛒 Gerenciamento de Vendas")
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        label.setFont(label_font)

        btn_nova_venda = QPushButton("➕ Nova Venda")
        btn_nova_venda.setMinimumHeight(40)

        btn_historico = QPushButton("📋 Histórico de Vendas")
        btn_historico.setMinimumHeight(40)

        layout.addWidget(label)
        layout.addWidget(btn_nova_venda)
        layout.addWidget(btn_historico)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_estoque_tab(self):
        """Cria a aba de Estoque"""
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("📦 Controle de Estoque")
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        label.setFont(label_font)

        btn_adicionar = QPushButton("➕ Adicionar Produto")
        btn_adicionar.setMinimumHeight(40)

        btn_listar = QPushButton("📋 Listar Produtos")
        btn_listar.setMinimumHeight(40)

        layout.addWidget(label)
        layout.addWidget(btn_adicionar)
        layout.addWidget(btn_listar)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_clientes_tab(self):
        """Cria a aba de Clientes"""
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("👥 Gerenciamento de Clientes")
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        label.setFont(label_font)

        form_layout = QVBoxLayout()

        self.cliente_nome = QLineEdit()
        self.cliente_nome.setPlaceholderText("Nome")
        self.cliente_cpf = QLineEdit()
        self.cliente_cpf.setPlaceholderText("CPF")
        self.cliente_email = QLineEdit()
        self.cliente_email.setPlaceholderText("E-mail")
        self.cliente_telefone = QLineEdit()
        self.cliente_telefone.setPlaceholderText("Telefone")
        self.cliente_endereco = QLineEdit()
        self.cliente_endereco.setPlaceholderText("Endereço")

        btn_novo_cliente = QPushButton("➕ Salvar Cliente")
        btn_novo_cliente.setMinimumHeight(40)
        btn_novo_cliente.clicked.connect(self.salvar_cliente)

        btn_listar_clientes = QPushButton("📋 Listar Clientes")
        btn_listar_clientes.setMinimumHeight(40)
        btn_listar_clientes.clicked.connect(self.listar_clientes)

        self.clientes_output = QTextEdit()
        self.clientes_output.setReadOnly(True)
        self.clientes_output.setPlaceholderText(
            "Clientes cadastrados aparecerão aqui...")

        form_layout.addWidget(self.cliente_nome)
        form_layout.addWidget(self.cliente_cpf)
        form_layout.addWidget(self.cliente_email)
        form_layout.addWidget(self.cliente_telefone)
        form_layout.addWidget(self.cliente_endereco)
        form_layout.addWidget(btn_novo_cliente)
        form_layout.addWidget(btn_listar_clientes)

        layout.addWidget(label)
        layout.addLayout(form_layout)
        layout.addWidget(self.clientes_output)
        layout.addStretch()

        widget.setLayout(layout)
        self.listar_clientes()
        return widget

    def salvar_cliente(self):
        """Salva um cliente no banco de dados."""
        nome = self.cliente_nome.text().strip()
        cpf = self.cliente_cpf.text().strip()
        email = self.cliente_email.text().strip()
        telefone = self.cliente_telefone.text().strip()
        endereco = self.cliente_endereco.text().strip()

        if not nome:
            QMessageBox.warning(
                self, "Cadastro", "O nome do cliente é obrigatório.")
            return

        try:
            self.db.save_cliente(nome, cpf, email, telefone, endereco)
            QMessageBox.information(
                self, "Cadastro", "Cliente cadastrado com sucesso!")
            self.cliente_nome.clear()
            self.cliente_cpf.clear()
            self.cliente_email.clear()
            self.cliente_telefone.clear()
            self.cliente_endereco.clear()
            self.listar_clientes()
        except Exception as exc:
            QMessageBox.critical(
                self, "Erro", f"Não foi possível salvar o cliente: {exc}")

    def listar_clientes(self):
        """Lista clientes cadastrados e mostra no campo de texto."""
        clientes = self.db.listar_clientes()
        if not clientes:
            self.clientes_output.setPlainText("Nenhum cliente cadastrado.")
            return

        texto = []
        for cliente in clientes:
            texto.append(
                f"ID: {cliente['id']} | Nome: {cliente['nome']} | CPF: {cliente['cpf'] or '-'} | "
                f"Telefone: {cliente['telefone'] or '-'} | E-mail: {cliente['email'] or '-'} | "
                f"Endereço: {cliente['endereco'] or '-'}"
            )

        self.clientes_output.setPlainText("\n".join(texto))

    def create_relatorios_tab(self):
        """Cria a aba de Relatórios"""
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("📈 Relatórios e Análises")
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        label.setFont(label_font)

        btn_vendas = QPushButton("📊 Relatório de Vendas")
        btn_vendas.setMinimumHeight(40)

        btn_estoque = QPushButton("📊 Relatório de Estoque")
        btn_estoque.setMinimumHeight(40)

        layout.addWidget(label)
        layout.addWidget(btn_vendas)
        layout.addWidget(btn_estoque)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

    def create_status_tab(self):
        """Cria a aba de status online do GitHub."""
        widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel("🌐 Status do projeto online")
        label_font = QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)
        label.setFont(label_font)

        self.status_online_label = QLabel("Verificando conexão...")
        self.status_online_label.setStyleSheet(
            "font-size: 18px; font-weight: bold;")

        self.status_url_label = QLabel("URL: https://github.com")
        self.status_url_label.setWordWrap(True)

        btn_verificar = QPushButton("🔄 Verificar Agora")
        btn_verificar.setMinimumHeight(40)
        btn_verificar.clicked.connect(self.atualizar_status_online)

        layout.addWidget(label)
        layout.addWidget(self.status_online_label)
        layout.addWidget(self.status_url_label)
        layout.addWidget(btn_verificar)
        layout.addStretch()

        widget.setLayout(layout)
        self.atualizar_status_online()
        return widget

    def atualizar_status_online(self):
        """Atualiza o status de disponibilidade do GitHub."""
        status = check_online_status()
        if status["online"]:
            texto = "✅ ONLINE"
            cor = "green"
        else:
            texto = "❌ OFFLINE"
            cor = "red"

        self.status_online_label.setText(texto)
        self.status_online_label.setStyleSheet(
            f"font-size: 18px; font-weight: bold; color: {cor};")
        self.status_url_label.setText(
            f"URL: {status['url']} | Status: {status['status']}")


def main():
    """Função principal"""
    app = QApplication(sys.argv)
    window = PDVMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
