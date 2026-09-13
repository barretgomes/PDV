# 📋 GUIA PASSO A PASSO - Conectar GitHub

## ⚠️ PRÉ-REQUISITOS

Antes de começar, você PRECISA de:

1. **Conta GitHub** (crie em https://github.com/signup se não tiver)
2. **Estar logado no GitHub** (abra https://github.com e verifique se está logado)

---

## 🚀 PASSO 1: Abrir PowerShell

1. Pressione: **`Win + R`**
2. Digite: **`powershell`**
3. Pressione: **ENTER**

```
PS C:\Users\rusla>
```

---

## 📂 PASSO 2: Ir para Pasta do PDV

**Cole este comando e pressione ENTER:**

```powershell
cd "c:\Users\rusla\OneDrive\Documentos\PDV"
```

**Saída esperada:**
```
PS C:\Users\rusla\OneDrive\Documentos\PDV>
```

---

## ✅ PASSO 3: Verificar Git (Opcional)

**Digite:**
```powershell
git status
```

**Saída esperada:**
```
On branch main
nothing to commit, working tree clean
```

Se der erro, o Git não está instalado. Instale em: https://git-scm.com/

---

## 🌐 PASSO 4: Criar Repositório no GitHub

**Abra seu navegador e acesse:**

https://github.com/new

**Preencha assim:**

```
Repository name:     PDV
Description:         Sistema de Ponto de Venda
Visibility:          Public (ou Private)
```

**⚠️ IMPORTANTE:**
- ❌ NÃO marque "Add a README file"
- ❌ NÃO marque "Add .gitignore"
- ✅ Clique em "Create repository"

**Você verá algo assim:**
```
…or push an existing repository from the command line

git remote add origin https://github.com/SEU_USUARIO/PDV.git
git branch -M main
git push -u origin main
```

---

## 🔗 PASSO 5: Configurar Remote (ESSENCIAL!)

**Volta ao PowerShell e cole este comando:**

```powershell
git remote add origin https://github.com/SEU_USUARIO/PDV.git
```

**⚠️ IMPORTANTE:** Substituir `SEU_USUARIO` pelo seu nome de usuário GitHub!

**Exemplo real:**
```powershell
git remote add origin https://github.com/joaosilva/PDV.git
```

**Saída esperada:** (sem mensagens de erro)
```
PS C:\Users\rusla\OneDrive\Documentos\PDV>
```

---

## ✔️ PASSO 6: Renomear Branch

**Cole este comando:**

```powershell
git branch -M main
```

**Saída esperada:** (nenhuma mensagem)
```
PS C:\Users\rusla\OneDrive\Documentos\PDV>
```

---

## 🔐 PASSO 7: Configurar Autenticação

Escolha UMA das opções abaixo:

### OPÇÃO A: GitHub CLI (MAIS FÁCIL - RECOMENDADO)

**a) Instale GitHub CLI:**
- Abra: https://cli.github.com/
- Clique em "Download" (Windows)
- Execute o instalador
- Reinicie o PowerShell

**b) Faça login:**

```powershell
gh auth login
```

**Respostas:**
```
? What account do you want to log into? 
> GitHub.com

? What is your preferred protocol for Git operations?
> HTTPS

? Authenticate Git with your GitHub credentials?
> Yes

? How would you like to authenticate GitHub CLI?
> Login with a web browser
```

Um navegador vai abrir - **clique em "Authorize"**

**Pronto! Você está autenticado!**

---

### OPÇÃO B: Token PAT (Se GitHub CLI não funcionar)

**a) Criar Token:**
- Acesse: https://github.com/settings/tokens
- Clique em "Generate new token (classic)"
- Preencha:
  - **Note:** PDV Local
  - **Expiration:** 90 days
  - **Scope:** marque ✅ `repo` (acesso completo)
- Clique em "Generate token"
- **COPIE o token** (mostra só uma vez!)

**b) Configurar Git:**

```powershell
git config --global credential.helper manager-core
```

---

## 🚀 PASSO 8: Fazer Push

**Cole este comando:**

```powershell
git push -u origin main
```

**O que vai acontecer:**

- Se usou GitHub CLI: push direto
- Se usou Token PAT: vai pedir senha (cole o token como senha)

**Saída esperada:**
```
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 5.23 KiB | 2.61 MiB/s, done.
Total 12 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'main' on GitHub by visiting:
remote:      https://github.com/SEU_USUARIO/PDV/pull/new/main
remote:
To https://github.com/SEU_USUARIO/PDV.git
 * [new branch]      main -> main
Branch 'main' is set up to track 'origin/main'.
```

---

## ✅ PASSO 9: Verificar Sucesso

**Cole este comando:**

```powershell
git remote -v
```

**Saída esperada:**
```
origin  https://github.com/SEU_USUARIO/PDV.git (fetch)
origin  https://github.com/SEU_USUARIO/PDV.git (push)
```

---

## 🎉 PRONTO!

Seu código está no GitHub! Acesse:

```
https://github.com/SEU_USUARIO/PDV
```

---

## 🆘 ERROS COMUNS

### Erro 1: "fatal: remote origin already exists"

**Solução:**
```powershell
git remote remove origin
# Depois rode o comando do PASSO 5 novamente
```

### Erro 2: "fatal: You are not currently on a branch"

**Solução:**
```powershell
git checkout -b main
git push -u origin main
```

### Erro 3: "Permission denied"

**Solução:**
- GitHub CLI não está autenticado
- Execute: `gh auth login`
- Ou use Token PAT (PASSO 7 OPÇÃO B)

### Erro 4: "fatal: The current branch main has no upstream branch"

**Solução:**
```powershell
git push -u origin main
```

---

## 📝 RESUMO DOS COMANDOS

```powershell
# 1. Ir para pasta
cd "c:\Users\rusla\OneDrive\Documentos\PDV"

# 2. Configurar remote (substituir SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/PDV.git

# 3. Renomear branch
git branch -M main

# 4. Fazer push
git push -u origin main
```

**Total: 4 linhas de comando!**

---

## 💡 DÚVIDAS?

**Qual é seu erro exato?** Escreva a mensagem completa para eu ajudar.

**Qual é seu nome de usuário GitHub?** Para fazer as substituições certas.
