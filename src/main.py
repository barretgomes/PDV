"""
Arquivo principal do Sistema de PDV
Ponto de Venda (PDV) - Sistema de Vendas Completo
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QTabWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class PDVMainWindow(QMainWindow):
    """Janela principal do sistema de PDV"""

    def __init__(self):
        super().__init__()
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

        btn_novo_cliente = QPushButton("➕ Novo Cliente")
        btn_novo_cliente.setMinimumHeight(40)

        btn_listar_clientes = QPushButton("📋 Listar Clientes")
        btn_listar_clientes.setMinimumHeight(40)

        layout.addWidget(label)
        layout.addWidget(btn_novo_cliente)
        layout.addWidget(btn_listar_clientes)
        layout.addStretch()

        widget.setLayout(layout)
        return widget

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


def main():
    """Função principal"""
    app = QApplication(sys.argv)
    window = PDVMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
