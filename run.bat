@echo off
REM PDV - Sistema de Ponto de Venda
REM Script executável para Windows

echo ================================
echo   PDV - Sistema de Vendas
echo ================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python não está instalado!
    echo    Instale em: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ %PYTHON_VERSION%
echo.

REM Criar ambiente virtual
if not exist "venv" (
    echo 📦 Criando ambiente virtual...
    python -m venv venv
)

REM Ativar ambiente virtual
echo ⚙️  Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Instalar dependências
echo 📚 Instalando dependências...
pip install -q -r requirements.txt

REM Executar sistema
echo.
echo 🎉 Iniciando PDV...
echo.
python src/main.py

pause
