#!/usr/bin/env python3
"""
Script para criar/editar release no GitHub usando a API
"""

import urllib.error
import urllib.request
import json
import sys
import subprocess
from pathlib import Path

# ===== CONFIGURAÇÃO =====
REPO_OWNER = "barretgomes"
REPO_NAME = "PDV"
TAG = "v1.0.0"
TOKEN = input(
    "Cole seu GitHub Personal Access Token (ou deixe vazio para tentar via Git): ").strip()

if not TOKEN:
    print("\n🔍 Tentando obter token via Git...")
    try:
        # Tenta extrair o token do git credential helper
        result = subprocess.run(
            ['git', 'credential', 'fill'],
            input=b'host=github.com\n\n',
            capture_output=True,
            text=False
        )
        if result.returncode == 0:
            lines = result.stdout.decode().split('\n')
            for line in lines:
                if line.startswith('password='):
                    TOKEN = line.split('=', 1)[1]
                    break
    except Exception as e:
        print(f"❌ Erro ao tentar obter token: {e}")

if not TOKEN:
    print("\n❌ Token não fornecido! Não é possível continuar.")
    print("\n📌 Como gerar um token:")
    print("1. Vá a https://github.com/settings/tokens")
    print("2. Clique 'Generate new token'")
    print("3. Selecione 'repo' scope")
    print("4. Copie o token")
    sys.exit(1)

# ===== DESCRIÇÃO DA RELEASE =====
RELEASE_NOTES = """# PDV v1.0.0 🎉

**Primeira versão do Sistema de Ponto de Venda (PDV)**

## ✨ Recursos

- 💳 **Gestão de Vendas**: Registre vendas e transações
- 📦 **Controle de Estoque**: Gerencie produtos e quantidades
- 👥 **Cadastro de Clientes**: Mantenha informações de clientes
- 📈 **Relatórios**: Visualize dados de vendas e estoque
- 💾 **Banco de Dados**: SQLite integrado

## 📋 Requisitos

- Python 3.8+
- PyQt5 5.15.9
- SQLite3 (incluído)

## 🚀 Como Usar

### Windows (Fácil)
```bash
PDV.exe
```

### Qualquer Sistema
```bash
python -m pip install -r requirements.txt
python src/main.py
```

## 📁 Estrutura do Projeto

```
PDV/
├── src/
│   ├── main.py           # Aplicação principal
│   ├── database/
│   │   └── db.py         # Gerenciador de banco de dados
│   └── __init__.py
├── tests/
├── requirements.txt      # Dependências
├── README.md            # Documentação
└── Makefile             # Automação
```

## 📝 Notas da Release

Esta é a primeira versão de produção do PDV. 

**Status**: ✅ Pronto para usar

### Próximas Features
- [ ] Integração com NFC
- [ ] Suporte a múltiplos usuários
- [ ] Backup automático na nuvem
- [ ] Aplicativo mobile
- [ ] Versão web

## 🙏 Suporte

Para reportar bugs ou sugerir melhorias:
- 📧 Email: barretgomes@example.com
- 🐛 GitHub Issues: https://github.com/barretgomes/PDV/issues

---

**Versão**: 1.0.0  
**Data**: 2026-09-13  
**Licença**: MIT
"""

# ===== UPLOAD PARA GITHUB =====
print(f"\n📤 Criando release para {REPO_OWNER}/{REPO_NAME}:{TAG}...\n")


url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/tags/{TAG}"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {TOKEN}",
    "User-Agent": "PDV-Release-Script"
}

# Dados da release
data = {
    "tag_name": TAG,
    "name": f"PDV {TAG}",
    "body": RELEASE_NOTES,
    "draft": False,
    "prerelease": False
}

try:
    # Tenta atualizar a release existente (PATCH)
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='PATCH'
    )

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read())
        print(f"✅ Release atualizada com sucesso!\n")
        print(f"📌 Nome: {result['name']}")
        print(f"🔖 Tag: {result['tag_name']}")
        print(f"📄 Body: {len(result['body'])} caracteres")
        print(f"🌐 URL: {result['html_url']}\n")

except urllib.error.HTTPError as e:
    error_data = json.loads(e.read())
    print(
        f"❌ Erro {e.code}: {error_data.get('message', 'Erro desconhecido')}\n")

    if e.code == 404:
        print("🔍 A release não existe ainda. Tentando criar uma nova...\n")

        # Remove 'draft' e 'prerelease' se quer criar nova
        data_create = {
            "tag_name": TAG,
            "name": f"PDV {TAG}",
            "body": RELEASE_NOTES,
            "draft": False,
            "prerelease": False
        }

        create_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases"
        req_create = urllib.request.Request(
            create_url,
            data=json.dumps(data_create).encode('utf-8'),
            headers=headers,
            method='POST'
        )

        try:
            with urllib.request.urlopen(req_create) as response:
                result = json.loads(response.read())
                print(f"✅ Release criada com sucesso!\n")
                print(f"📌 Nome: {result['name']}")
                print(f"🔖 Tag: {result['tag_name']}")
                print(f"📄 Body: {len(result['body'])} caracteres")
                print(f"🌐 URL: {result['html_url']}\n")
        except Exception as e2:
            print(f"❌ Erro ao criar release: {e2}")
    else:
        print(f"❌ Erro na solicitação: {error_data}")

except Exception as e:
    print(f"❌ Erro: {e}")

print("\n✨ Pronto! Acesse: https://github.com/barretgomes/PDV/releases")
