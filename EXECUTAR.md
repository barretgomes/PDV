# 🚀 Como Executar o PDV

## ✅ OPÇÃO 1: Script Rápido (MAIS FÁCIL)

### Windows
**Clique duas vezes em:**
```
run.bat
```

### Linux/Mac
**Execute no terminal:**
```bash
chmod +x run.sh
./run.sh
```

**O que faz:**
- ✅ Cria ambiente virtual automaticamente
- ✅ Instala dependências
- ✅ Executa o PDV

---

## ✅ OPÇÃO 2: Make Commands

Se tiver `make` instalado (ou `mingw32-make` no Windows):

```bash
# Ver todos os comandos
make help

# Executar
make run

# Testes
make test

# Build executável
make build
```

---

## ✅ OPÇÃO 3: Executável Compilado

### Criar executável:

**Windows/Linux/Mac:**
```bash
python build.py
```

Ou manualmente:
```bash
pip install pyinstaller
python build.py
```

**Resultado:**
```
dist/PDV          (Linux/Mac)
dist/PDV.exe      (Windows)
```

**Executar:**
```bash
# Windows
.\dist\PDV.exe

# Linux/Mac
./dist/PDV
```

---

## ✅ OPÇÃO 4: Manual

```bash
# 1. Criar ambiente virtual
python -m venv venv

# 2. Ativar (Windows)
venv\Scripts\activate

# 2. Ativar (Linux/Mac)
source venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar
python src/main.py
```

---

## 🌐 GitHub Actions (Automático)

A cada `push` no GitHub:

✅ Testes rodam automaticamente
✅ Código é verificado (linting)
✅ Executável é compilado
✅ Release é criada (em tags)

**Veja em:**
```
https://github.com/barretgomes/PDV/actions
```

---

## 📦 Fazer Build e Enviar para GitHub

### 1. Fazer mudanças no código

```bash
# Editar arquivos...
```

### 2. Commit e Push

```bash
git add .
git commit -m "feat: descrição da mudança"
git push
```

### 3. GitHub Actions Executa Automaticamente

- 🧪 Testes rodam
- 🔍 Código é verificado
- 🔨 Executável é criado

**Veja em:** https://github.com/barretgomes/PDV/actions

---

## 🏷️ Criar Release com Executável

### 1. Fazer tag

```bash
git tag -a v1.0.0 -m "Release 1.0.0"
git push origin v1.0.0
```

### 2. GitHub cria Release automaticamente

Com o executável anexado!

**Veja em:** https://github.com/barretgomes/PDV/releases

---

## ⚙️ Requisitos

| Opção | Python | PyQt5 | PyInstaller |
|-------|--------|-------|-------------|
| run.bat/run.sh | ✅ Sim | ✅ Automático | ❌ Não |
| Executável (build.py) | ✅ Sim | ✅ Automático | ✅ Sim |
| Manual | ✅ Sim | ✅ Manual | ❌ Não |

---

## 🆘 Erros Comuns

### Erro: "Python não encontrado"
```bash
# Instale Python: https://python.org
# Certifique-se de adicionar ao PATH
```

### Erro: "ModuleNotFoundError: No module named 'PyQt5'"
```bash
pip install -r requirements.txt
```

### Erro ao compilar executável
```bash
pip install --upgrade pyinstaller
python build.py
```

---

## 💡 Próximas Etapas

1. ✅ Executar o PDV localmente
2. ✅ Fazer mudanças e commit
3. ✅ Push para GitHub
4. ✅ GitHub Actions testa automaticamente
5. ✅ Criar release com executável

**Bora codar! 🚀**
