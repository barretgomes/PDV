#!/usr/bin/env python3
"""
Upload files to GitHub Release v1.0.0
"""

import os
import subprocess
import json

# Verificar se os arquivos existem
dist_path = "dist/PDV.exe"
zip_path = "PDV-v1.0.0.zip"

print("📦 Preparando arquivos para upload...\n")

if not os.path.exists(dist_path):
    print(f"❌ Erro: {dist_path} não encontrado!")
    exit(1)

if not os.path.exists(zip_path):
    print(f"❌ Erro: {zip_path} não encontrado!")
    exit(1)

print(
    f"✅ Encontrado: {dist_path} ({os.path.getsize(dist_path) / (1024*1024):.1f} MB)")
print(
    f"✅ Encontrado: {zip_path} ({os.path.getsize(zip_path) / (1024*1024):.1f} MB)\n")

# Informações da release
OWNER = "barretgomes"
REPO = "PDV"
TAG = "v1.0.0"

print(f"🌐 Repository: {OWNER}/{REPO}")
print(f"🔖 Tag: {TAG}\n")

# Tentar usar gh CLI
print("📤 Tentando usar GitHub CLI...\n")

try:
    # Verificar se gh está disponível
    result = subprocess.run(
        ["gh", "--version"],
        capture_output=True,
        text=True,
        timeout=5
    )

    if result.returncode == 0:
        print(f"✅ GitHub CLI disponível: {result.stdout.strip()}\n")

        # Fazer upload dos arquivos
        print(f"📤 Fazendo upload de {dist_path}...")

        try:
            subprocess.run(
                ["gh", "release", "upload", TAG, dist_path,
                    "-R", f"{OWNER}/{REPO}", "--clobber"],
                timeout=120,
                check=True
            )
            print(f"✅ {dist_path} enviado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Erro ao fazer upload de {dist_path}: {e}")

        print(f"\n📤 Fazendo upload de {zip_path}...")

        try:
            subprocess.run(
                ["gh", "release", "upload", TAG, zip_path,
                    "-R", f"{OWNER}/{REPO}", "--clobber"],
                timeout=120,
                check=True
            )
            print(f"✅ {zip_path} enviado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Erro ao fazer upload de {zip_path}: {e}")

        print("\n✨ Upload concluído!")
        print(
            f"\n🌐 Acesse: https://github.com/{OWNER}/{REPO}/releases/tag/{TAG}")

    else:
        raise Exception("gh CLI não respondeu")

except Exception as e:
    print(f"⚠️  GitHub CLI não disponível: {e}")
    print("\n📌 Para fazer upload manual:")
    print(
        f"   1. Acesse: https://github.com/{OWNER}/{REPO}/releases/tag/{TAG}")
    print(f"   2. Clique em 'Edit'")
    print(f"   3. Arraste ou selecione os arquivos:")
    print(f"      - {dist_path}")
    print(f"      - {zip_path}")
    print(f"   4. Clique em 'Update release'")
    print(f"\n   Arquivos prontos em:")
    print(f"   - {os.path.abspath(dist_path)}")
    print(f"   - {os.path.abspath(zip_path)}")
