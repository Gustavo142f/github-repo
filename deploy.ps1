# Deploy script para GitHub
# Script PowerShell para automatizar o push do repositório

# Configurações
$REPO_URL = "https://github.com/Gustavo142f/github-repo.git"
$REPO_DIR = $PSScriptRoot

# Cores para output
$GREEN = "`e[32m"
$RED = "`e[31m"
$YELLOW = "`e[33m"
$BLUE = "`e[34m"
$RESET = "`e[0m"

function Write-Success {
    Write-Host "$GREEN✅ $args$RESET"
}

function Write-Error {
    Write-Host "$RED❌ $args$RESET"
}

function Write-Info {
    Write-Host "$BLUE ℹ️  $args$RESET"
}

function Write-Step {
    Write-Host "$YELLOW➤ $args$RESET"
}

# Verificar se git está instalado
Write-Step "Verificando se Git está instalado..."
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git não está instalado!"
    Write-Info "Visite: https://git-scm.com/download/win"
    Write-Info "Leia: DEPLOY_GITHUB.md para instruções completas"
    exit 1
}

Write-Success "Git encontrado"

# Ir para o diretório
cd $REPO_DIR
Write-Info "Diretório: $REPO_DIR"

# 1. Inicializar git (se não houver .git)
Write-Step "Passo 1: Inicializando repositório..."
if (-not (Test-Path .git)) {
    git init
    Write-Success "Repositório inicializado"
} else {
    Write-Info "Repositório já existe"
}

# 2. Configurar user (opcional, pula se já configurado)
Write-Step "Passo 2: Verificando configuração Git..."
$gitUserName = git config user.name 2>$null
$gitUserEmail = git config user.email 2>$null

if (-not $gitUserName -or -not $gitUserEmail) {
    Write-Info "Configuração de usuário não encontrada"
    Write-Info "Use: git config --global user.name 'Seu Nome'"
    Write-Info "Use: git config --global user.email 'seu.email@github.com'"
}

# 3. Adicionar arquivos
Write-Step "Passo 3: Adicionando arquivos..."
git add .
Write-Success "Arquivos adicionados"

# 4. Verificar status
$status = git status --porcelain
if ($status) {
    Write-Info "Arquivos modificados detectados"
} else {
    Write-Info "Nenhum arquivo modificado"
}

# 5. Commit
Write-Step "Passo 4: Criando commit..."
git commit -m "Initial commit: Organize Python learning modules" -q 2>$null
if ($LASTEXITCODE -eq 0 -or $LASTEXITCODE -eq 1) {
    Write-Success "Commit criado"
} else {
    Write-Info "Nenhuma mudança para commitar"
}

# 6. Configurar remote
Write-Step "Passo 5: Configurando remote..."
$remoteExists = git remote | Select-String "^origin`$"
if (-not $remoteExists) {
    git remote add origin $REPO_URL
    Write-Success "Remote 'origin' configurado"
} else {
    Write-Info "Remote 'origin' já configurado"
}

# 7. Renomear branch para main
Write-Step "Passo 6: Preparando branch principal..."
git branch -M main 2>$null
Write-Success "Branch renomeado para 'main'"

# 8. Push
Write-Step "Passo 7: Fazendo push para GitHub..."
Write-Info "Se solicitado, use seu token de acesso pessoal como senha"
Write-Info "Gere um token em: https://github.com/settings/tokens"

git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Success "Push realizado com sucesso!"
    Write-Success "Seu repositório está em: $REPO_URL"
} else {
    Write-Error "Erro ao fazer push"
    Write-Info "Verifique suas credenciais de autenticação"
    Write-Info "Leia: DEPLOY_GITHUB.md para mais informações"
    exit 1
}

Write-Host ""
Write-Host "$GREEN╔════════════════════════════════════════╗$RESET"
Write-Host "$GREEN║   ✅ Deploy realizado com sucesso!    ║$RESET"
Write-Host "$GREEN╚════════════════════════════════════════╝$RESET"
Write-Host ""
Write-Host "🔗 Repositório: $REPO_URL"
Write-Host "📁 Diretório local: $REPO_DIR"
Write-Host ""
Write-Host "📝 Próximos passos:"
Write-Host "  1. Faça alterações nos arquivos"
Write-Host "  2. Execute: git add ."
Write-Host "  3. Execute: git commit -m 'Descrição'"
Write-Host "  4. Execute: git push"
Write-Host ""
