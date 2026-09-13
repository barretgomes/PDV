#!/bin/bash
# PDV - Sistema de Ponto de Venda
# Script executável para rodar o sistema

set -e

echo "================================"
echo "  🚀 PDV - Sistema de Vendas"
echo "================================"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não está instalado!"
    echo "   Instale em: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Criar ambiente virtual
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "⚙️  Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install -q -r requirements.txt

# Executar o sistema
echo ""
echo "🎉 Iniciando PDV..."
echo ""
python3 src/main.py

deactivate
