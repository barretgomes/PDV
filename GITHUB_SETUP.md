# 🚀 Guia Completo: Integração Git + GitHub

## PASSO 1: Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha assim:
   - **Repository name:** `PDV`
   - **Description:** `Sistema de Ponto de Venda (PDV) com Python e PyQt5`
   - **Visibility:** Public ou Private (sua escolha)
   - **❌ NÃO** marque "Add a README file" (já temos um)
   - **❌ NÃO** marque "Add .gitignore" (já temos um)
3. Clique em "Create repository"

---

## PASSO 2: Configurar Credenciais Git (Windows)

### Opção A: Usar Token PAT (Recomendado)

1. No GitHub, vá para: **Settings → Developer settings → Personal access tokens**
2. Clique em "Generate new token (classic)"
3. Preencha:
   - **Note:** PDV Local
   - **Expiration:** 90 days
   - **Scopes:** Marque `repo` (acesso completo aos repos)
4. Copie o token (você só vê uma vez!)

### Opção B: Usar GitHub CLI (Mais Fácil)

```powershell
# Baixe e instale: https://cli.github.com/
# Depois execute:
gh auth login

# Escolha as opções:
# - GitHub.com
# - HTTPS
# - Y (authenticate Git with your GitHub credentials)
```

---

## PASSO 3: Adicionar Remote do GitHub

**Abra o PowerShell e execute:**

```powershell
cd "c:\Users\rusla\OneDrive\Documentos\PDV"

# Substituir SEU_USUARIO pelo seu nome de usuário GitHub
git remote add origin https://github.com/SEU_USUARIO/PDV.git

# Renomear branch para 'main' (padrão GitHub)
git branch -M main

# Fazer push do código
git push -u origin main
```

**Exemplo completo:**
```powershell
cd "c:\Users\rusla\OneDrive\Documentos\PDV"
git remote add origin https://github.com/seu-usuario/PDV.git
git branch -M main
git push -u origin main
```

---

## PASSO 4: Verificar Integração

```powershell
# Ver remotes configurados
git remote -v

# Verificar status
git status
```

**Saída esperada:**
```
origin  https://github.com/seu-usuario/PDV.git (fetch)
origin  https://github.com/seu-usuario/PDV.git (push)
On branch main
Your branch is up to date with 'origin/main'.
```

---

## PASSO 5: Workflow Diário

Após integração, seus commands serão:

```powershell
# Editar arquivos...

# Ver mudanças
git status
git diff

# Commit
git add .
git commit -m "Descrição das mudanças"

# Enviar para GitHub
git push
```

---

## 🆘 Troubleshooting

### Erro: "fatal: remote origin already exists"
```powershell
git remote remove origin
# Depois rode git remote add origin... novamente
```

### Erro: "Authentication failed"
- Use token PAT ao invés de senha
- Ou configure `gh auth login`

### Erro: "fatal: You are not currently on a branch"
```powershell
git checkout -b main
git push -u origin main
```

---

## ✅ Checklist Final

- [ ] Repositório criado no GitHub
- [ ] Credenciais configuradas (Token ou GitHub CLI)
- [ ] Remote adicionado (`git remote -v`)
- [ ] Push realizado com sucesso (`git push`)
- [ ] Arquivos visíveis em https://github.com/seu-usuario/PDV

---

## 📚 Recursos Úteis

- **Git Docs:** https://git-scm.com/doc
- **GitHub Docs:** https://docs.github.com
- **GitHub CLI:** https://cli.github.com/
- **Generate PAT:** https://github.com/settings/tokens
