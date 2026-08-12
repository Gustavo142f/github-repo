#!/bin/bash
# Deploy script para GitHub (Linux/macOS)
# Execute: bash deploy.sh

set -e  # Exit on error

# Configurações
REPO_URL="https://github.com/Gustavo142f/github-repo.git"
REPO_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     Git Deploy para GitHub Script      ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════╝${NC}"
echo ""

# Verificar git
echo -e "${YELLOW}➤${NC} Verificando se Git está instalado..."
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git não está instalado!${NC}"
    echo -e "${BLUE}ℹ️  Visite: https://git-scm.com/download/linux${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Git encontrado${NC}"

# Ir para o diretório
cd "$REPO_DIR"
echo -e "${BLUE}ℹ️  Diretório: $REPO_DIR${NC}"

# 1. Inicializar git
echo ""
echo -e "${YELLOW}➤${NC} Passo 1: Inicializando repositório..."
if [ ! -d .git ]; then
    git init
    echo -e "${GREEN}✅ Repositório inicializado${NC}"
else
    echo -e "${BLUE}ℹ️  Repositório já existe${NC}"
fi

# 2. Configurar user
echo ""
echo -e "${YELLOW}➤${NC} Passo 2: Verificando configuração Git..."
GIT_USER=$(git config user.name 2>/dev/null || echo "")
GIT_EMAIL=$(git config user.email 2>/dev/null || echo "")

if [ -z "$GIT_USER" ] || [ -z "$GIT_EMAIL" ]; then
    echo -e "${BLUE}ℹ️  Configure seu usuário:${NC}"
    echo -e "${BLUE}   git config --global user.name 'Seu Nome'${NC}"
    echo -e "${BLUE}   git config --global user.email 'seu.email@github.com'${NC}"
fi

# 3. Adicionar arquivos
echo ""
echo -e "${YELLOW}➤${NC} Passo 3: Adicionando arquivos..."
git add .
echo -e "${GREEN}✅ Arquivos adicionados${NC}"

# 4. Commit
echo ""
echo -e "${YELLOW}➤${NC} Passo 4: Criando commit..."
if git commit -m "Initial commit: Organize Python learning modules" 2>/dev/null; then
    echo -e "${GREEN}✅ Commit criado${NC}"
else
    echo -e "${BLUE}ℹ️  Nenhuma mudança para commitar${NC}"
fi

# 5. Configurar remote
echo ""
echo -e "${YELLOW}➤${NC} Passo 5: Configurando remote..."
if ! git remote | grep -q "^origin$"; then
    git remote add origin "$REPO_URL"
    echo -e "${GREEN}✅ Remote 'origin' configurado${NC}"
else
    echo -e "${BLUE}ℹ️  Remote 'origin' já configurado${NC}"
fi

# 6. Renomear branch
echo ""
echo -e "${YELLOW}➤${NC} Passo 6: Preparando branch principal..."
git branch -M main 2>/dev/null || true
echo -e "${GREEN}✅ Branch renomeado para 'main'${NC}"

# 7. Push
echo ""
echo -e "${YELLOW}➤${NC} Passo 7: Fazendo push para GitHub..."
echo -e "${BLUE}ℹ️  Se solicitado, use seu token de acesso pessoal${NC}"
echo -e "${BLUE}   Gere em: https://github.com/settings/tokens${NC}"
echo ""

if git push -u origin main; then
    echo ""
    echo -e "${GREEN}╔════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║   ✅ Deploy realizado com sucesso!    ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}🔗 Repositório:${NC} $REPO_URL"
    echo -e "${BLUE}📁 Diretório:${NC} $REPO_DIR"
    echo ""
    echo -e "${BLUE}📝 Próximos passos:${NC}"
    echo -e "   1. Faça alterações nos arquivos"
    echo -e "   2. Execute: ${YELLOW}git add .${NC}"
    echo -e "   3. Execute: ${YELLOW}git commit -m 'Descrição'${NC}"
    echo -e "   4. Execute: ${YELLOW}git push${NC}"
    echo ""
else
    echo -e "${RED}❌ Erro ao fazer push${NC}"
    echo -e "${BLUE}ℹ️  Verifique suas credenciais de autenticação${NC}"
    exit 1
fi
