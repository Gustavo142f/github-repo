# 🚀 Instruções de Deploy para GitHub

Git não está instalado no seu sistema. Siga os passos abaixo para fazer o deploy.

## ✅ Passo 1: Instalar Git

### Windows
1. Acesse: https://git-scm.com/download/win
2. Baixe e execute o instalador
3. Siga as instruções (use as configurações padrão)
4. Reinicie o PowerShell ou CMD

### macOS
```bash
brew install git
```

### Linux
```bash
sudo apt-get install git
```

---

## 📋 Passo 2: Configurar Git (execute uma única vez)

Após instalar git, execute:

```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

Substitua:
- `Seu Nome` pelo seu nome real
- `seu.email@example.com` pelo seu email do GitHub

---

## 🔧 Passo 3: Fazer o Deploy (em um terminal)

### Abra PowerShell ou CMD

Navegue até a pasta do projeto:
```powershell
cd c:\Users\gusta\workspace\github-repo
```

### 3.1 - Inicializar repositório git
```powershell
git init
```

### 3.2 - Adicionar todos os arquivos
```powershell
git add .
```

### 3.3 - Criar o primeiro commit
```powershell
git commit -m "Initial commit: Organize Python learning modules"
```

### 3.4 - Adicionar o remote (GitHub)
```powershell
git remote add origin https://github.com/Gustavo142f/github-repo.git
```

### 3.5 - Fazer o push para main
```powershell
git branch -M main
git push -u origin main
```

---

## 🔐 Passo 4: Autenticação (se solicitado)

Se pedir autenticação:

### Opção A: Token de Acesso Pessoal (Recomendado)

1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token"
3. Selecione "Generate new token (classic)"
4. Configure:
   - Nome: "GitHub Deploy"
   - Expiração: "No expiration" ou escolha um período
   - Scopes: Selecione ✓ `repo` (full control of private repositories)
5. Clique em "Generate token"
6. **Copie o token** (você nunca mais poderá vê-lo)
7. Cole o token quando o git pedir a senha

### Opção B: SSH (Alternativa)

Se preferir SSH, siga: https://docs.github.com/pt/authentication/connecting-to-github-with-ssh

---

## 📤 Passo 5: Verificar o Push

Após fazer o push:

1. Acesse: https://github.com/Gustavo142f/github-repo
2. Você deve ver:
   - ✅ Todos os arquivos listados
   - ✅ A mensagem do commit
   - ✅ Estrutura de pastas correta

---

## 🔄 Próximos Pushes (mais simples)

Depois que o primeiro push é feito, para adicionar mudanças:

```powershell
git add .
git commit -m "Descrição das mudanças"
git push
```

---

## 🆘 Troubleshooting

### "fatal: not a git repository"
→ Execute `git init` primeiro

### "fatal: The current branch main has no upstream branch"
→ Execute `git push -u origin main`

### "fatal: 'origin' does not appear to be a 'git' repository"
→ Execute `git remote add origin https://github.com/Gustavo142f/github-repo.git`

### "remote: Permission denied"
→ Verifique o token de acesso ou credenciais SSH

### "error: src refspec main does not match any branch"
→ Você precisa fazer pelo menos um commit primeiro:
```powershell
git add .
git commit -m "Initial commit"
```

---

## 📝 Exemplo Completo (copie e cole)

```powershell
# Ir para a pasta
cd c:\Users\gusta\workspace\github-repo

# Inicializar
git init

# Adicionar todos os arquivos
git add .

# Primeiro commit
git commit -m "Initial commit: Organize Python learning modules"

# Configurar remote
git remote add origin https://github.com/Gustavo142f/github-repo.git

# Renomear branch para main (se necessário)
git branch -M main

# Push
git push -u origin main
```

---

## 🎉 Pronto!

Seu repositório estará no GitHub! 

Próximas vezes é só:
```powershell
git add .
git commit -m "Descrição"
git push
```

---

## 📚 Recursos Úteis

- Git Docs: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/pt
- Git Cheat Sheet: https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf

---

**Boa sorte! 🚀**
