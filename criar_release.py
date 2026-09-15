#!/usr/bin/env python3
"""Criar arquivo ZIP para release do PDV"""

import shutil
import os
import webbrowser
from pathlib import Path

print("📦 Criando arquivo para release...\n")

# Caminhos
src_folder = Path("dist_release")
zip_path = "PDV-v1.0.0"

# Limpar se existir
if src_folder.exists():
    shutil.rmtree(src_folder)

# Criar pasta temporária
src_folder.mkdir()

# Copiar arquivos
print("📄 Copiando arquivos...")
shutil.copytree("src", src_folder / "src", dirs_exist_ok=True)
shutil.copy("README.md", src_folder / "README.md")
shutil.copy("requirements.txt", src_folder / "requirements.txt")
shutil.copy("EXECUTAR.md", src_folder / "EXECUTAR.md")

# Criar ZIP
print("📦 Compactando...")
shutil.make_archive(zip_path, 'zip', '.', src_folder)

print(f"✅ Arquivo criado: {zip_path}.zip\n")
print("🌐 Abrindo página de release no navegador...\n")

# Abrir no navegador
url = "https://github.com/barretgomes/PDV/releases/tag/v1.0.0"
webbrowser.open(url)

print(f"📌 Link: {url}")
print("\n📋 Instruções:")
print("1. Faça login no GitHub (se pedido)")
print("2. Clique em '✏️ Edit' (ícone de lápis)")
print("3. Preencha:")
print("   - Release title: PDV v1.0.0")
print("   - Description: (veja abaixo)")
print("4. Clique em 'Attach binaries' e selecione: PDV-v1.0.0.zip")
print("5. Clique em 'Update release'")

# Limpar temporário
shutil.rmtree(src_folder)
print("\n✨ Pronto!")
