#!/usr/bin/env python3
"""
Build script para criar executável do PDV
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description=""):
    """Executa um comando e trata erros"""
    print(f"\n{'='*50}")
    if description:
        print(f"  {description}")
    print(f"{'='*50}")
    print(f"Executando: {cmd}\n")

    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Erro ao executar: {cmd}")
        return False
    return True


def main():
    """Função principal"""
    print("\n🔨 PDV Build Script\n")

    # Verificar Python
    print("🔍 Verificando Python...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ requerido!")
        return False
    print(f"✅ Python {sys.version.split()[0]} encontrado\n")

    # Instalar PyInstaller
    print("📦 Instalando PyInstaller...")
    if not run_command("pip install pyinstaller", "Instalando PyInstaller"):
        return False

    # Criar diretório de build
    Path("build").mkdir(exist_ok=True)
    Path("dist").mkdir(exist_ok=True)

    # Configurar PyInstaller
    cmd = (
        "pyinstaller "
        "--name=PDV "
        "--windowed "
        "--onefile "
        "--distpath=dist "
        "--buildpath=build "
        "--specpath=build "
        "--hidden-import=PyQt5 "
        "--hidden-import=sqlite3 "
        "src/main.py"
    )

    if not run_command(cmd, "Compilando executável"):
        return False

    print("\n" + "="*50)
    print("  ✅ Build Concluído!")
    print("="*50)
    print(f"\n📂 Executável salvo em: ./dist/PDV")
    print(f"\n🚀 Para executar:")
    print(f"   Windows: .\\dist\\PDV.exe")
    print(f"   Linux/Mac: ./dist/PDV")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
