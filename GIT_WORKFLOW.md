# 📋 Guia de Boas Práticas Git - PDV

## 📌 Convenção de Commits

Siga o padrão **Conventional Commits**:

```
<tipo>(<escopo>): <assunto>

<corpo>

<rodapé>
```

### Tipos de Commit

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Alterações em documentação
- **style**: Formatação, espaçamento (não altera lógica)
- **refactor**: Refatoração de código
- **perf**: Melhoria de performance
- **test**: Adicionar ou atualizar testes
- **chore**: Atualizar dependências, config, etc

### Exemplos

```bash
# Nova feature
git commit -m "feat(vendas): adicionar cálculo de desconto"

# Correção
git commit -m "fix(estoque): corrigir atualização de quantidade"

# Documentação
git commit -m "docs(README): adicionar instruções de instalação"

# Refactor
git commit -m "refactor(database): melhorar tratamento de erros"

# Com corpo detalhado
git commit -m "feat(clientes): adicionar filtro por CPF

- Permite buscar clientes por CPF
- Valida formato do CPF
- Retorna erro se CPF é inválido

Closes #15"
```

---

## 🔀 Estratégia de Branches

```
main (produção)
  ↑
  └── release/1.0.0 (preparação para release)
       ↑
       └── develop (desenvolvimento)
            ↑
            ├── feature/vendas-desconto
            ├── feature/estoque-alerta
            ├── bugfix/login-erro
            └── ...
```

### Nomes de Branches

```
feature/nome-da-funcionalidade
bugfix/nome-do-bug
hotfix/nome-urgente
refactor/nome-refactor
docs/nome-doc
```

### Exemplos

```bash
# Criar branch de feature
git checkout -b feature/vendas-desconto
git checkout -b feature/sistema-notificacoes

# Criar branch de bugfix
git checkout -b bugfix/erro-autenticacao

# Criar branch de hotfix (urgente para produção)
git checkout -b hotfix/erro-critico-venda
```

---

## 📝 Workflow de Desenvolvimento

### 1. Iniciar Nova Feature

```bash
# Atualizar develop
git checkout develop
git pull origin develop

# Criar branch de feature
git checkout -b feature/minha-funcionalidade

# Fazer mudanças e commits
git add .
git commit -m "feat(vendas): adicionar desconto progressivo"
```

### 2. Manter Branch Atualizada

```bash
# Trazer mudanças de develop
git fetch origin
git rebase origin/develop

# Ou fazer merge (menos limpo, mas mais seguro)
git merge origin/develop
```

### 3. Preparar Pull Request

```bash
# Push da branch para GitHub
git push -u origin feature/minha-funcionalidade

# Abrir PR no GitHub
# - Vá para https://github.com/seu-usuario/PDV
# - Clique em "New Pull Request"
# - Compare sua branch com 'develop'
# - Descreva suas mudanças
# - Clique em "Create Pull Request"
```

### 4. Merge para Develop

```bash
# (Após aprovação no PR)

# Atualizar develop local
git checkout develop
git pull origin develop

# Fazer merge de sua branch
git merge feature/minha-funcionalidade

# Push para GitHub
git push origin develop

# Deletar branch (opcional)
git branch -d feature/minha-funcionalidade
git push origin --delete feature/minha-funcionalidade
```

---

## 🚀 Release e Produção

### Criar Release

```bash
# Criar branch de release a partir de develop
git checkout -b release/1.0.0 develop

# Fazer ajustes finais, updates de versão
# Testar tudo

# Fazer merge em main
git checkout main
git merge --no-ff release/1.0.0

# Criar tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push
git push origin main --tags

# Fazer merge de volta em develop
git checkout develop
git merge --no-ff release/1.0.0

git push origin develop
```

### Hotfix Urgente

```bash
# Criar hotfix a partir de main
git checkout -b hotfix/1.0.1 main

# Fazer correção
git commit -m "fix(critico): corrigir erro de venda"

# Merge em main
git checkout main
git merge --no-ff hotfix/1.0.1
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git push origin main --tags

# Merge em develop
git checkout develop
git merge --no-ff hotfix/1.0.1
git push origin develop
```

---

## 🛠️ Comandos Úteis

```bash
# Ver histórico
git log --oneline
git log --graph --all --decorate

# Ver branches
git branch -a
git branch -v

# Ver diferenças
git diff                    # Mudanças não staged
git diff --staged          # Mudanças staged
git diff main..feature/    # Diferenças entre branches

# Desfazer mudanças
git checkout -- arquivo    # Desfazer arquivo específico
git reset HEAD~1           # Desfazer último commit (local)
git revert HEAD            # Criar novo commit revertendo

# Limpar
git clean -fd              # Remover arquivos não rastreados
git reflog                 # Ver histórico de reset
```

---

## ✅ Checklist Antes de Push

- [ ] Código testado localmente
- [ ] Testes passando: `pytest tests/`
- [ ] Código formatado: `black src/`
- [ ] Sem warnings: `flake8 src`
- [ ] Commits com mensagens claras
- [ ] Sem dados sensíveis (senhas, tokens)
- [ ] Arquivo `.env` não commitado
- [ ] Banco de dados local não commitado

---

## 🔐 Segurança

### Não commitar

```
- Senhas, tokens, chaves
- Arquivos `.env` com dados sensíveis
- Arquivos grandes (>100MB)
- Arquivos binários desnecessários
```

### Proteger informações sensíveis

```bash
# Usar variáveis de ambiente
export DATABASE_URL="postgresql://user:pass@host/db"

# Usar arquivo .env local (não commitado)
# .env (não faça push!)
# DATABASE_URL=...

# Usar secrets no GitHub
# Actions → Secrets → New repository secret
```

---

## 📚 Recursos

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Docs](https://docs.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
