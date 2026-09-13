# 📌 PASSO A PASSO - GIT BASH + GITHUB

## 1️⃣ ABRIR GIT BASH

Clique com botão direito em qualquer pasta e escolha:
```
Git Bash Here
```

Ou procure na barra de iniciar por "Git Bash"

---

## 2️⃣ ENTRAR NA PASTA DO PDV

**Cole este comando:**
```bash
cd "/c/Users/rusla/OneDrive/Documentos/PDV"
```

Pressione **ENTER**

---

## 3️⃣ VERIFICAR SE ESTÁ TUDO BEM

**Cole:**
```bash
git status
```

Pressione **ENTER**

Deve aparecer:
```
On branch main
nothing to commit, working tree clean
```

---

## 4️⃣ ADICIONAR REMOTE DO GITHUB

**ANTES: Substitua `SEU_USUARIO` pelo seu usuário GitHub**

Exemplo: se seu usuário é `joaosilva`, fica assim:
```bash
git remote add origin https://github.com/joaosilva/PDV.git
```

**Cole o comando (com SUA username):**
```bash
git remote add origin https://github.com/SEU_USUARIO/PDV.git
```

Pressione **ENTER**

---

## 5️⃣ RENOMEAR BRANCH PARA MAIN

**Cole:**
```bash
git branch -M main
```

Pressione **ENTER**

---

## 6️⃣ FAZER PUSH PARA GITHUB

**Cole:**
```bash
git push -u origin main
```

Pressione **ENTER**

**Se pedir username/senha:**
- Username: seu usuário GitHub
- Password: seu token do GitHub

---

## ✅ PRONTO!

Seu código está no GitHub!

Acesse: `https://github.com/SEU_USUARIO/PDV`

---

## 📝 RESUMO (4 COMANDOS SÓ)

```bash
cd "/c/Users/rusla/OneDrive/Documentos/PDV"
git remote add origin https://github.com/SEU_USUARIO/PDV.git
git branch -M main
git push -u origin main
```

---

## 🔑 IMPORTANTE

1. **Substitua `SEU_USUARIO`** pelo seu usuário GitHub real
2. **GitHub CLI precisa estar instalado** - baixe em: https://cli.github.com/
3. **Faça login primeiro:**
   ```bash
   gh auth login
   ```
   Escolha HTTPS e deixar fazer login pelo navegador
