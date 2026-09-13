# Script de Integração Git + GitHub
# Execute este arquivo no PowerShell para integração automática

Write-Host "================================" -ForegroundColor Cyan
Write-Host "  🚀 PDV - Integração GitHub" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Perguntar pelo nome de usuário
$github_user = Read-Host "Digite seu nome de usuário GitHub"

if ([string]::IsNullOrWhiteSpace($github_user)) {
    Write-Host "❌ Nome de usuário não pode estar vazio!" -ForegroundColor Red
    exit
}

$repo_url = "https://github.com/$github_user/PDV.git"

Write-Host ""
Write-Host "Configurando integração:" -ForegroundColor Yellow
Write-Host "  - Usuário: $github_user"
Write-Host "  - URL: $repo_url"
Write-Host ""

# Verificar se remote já existe
$remote_exists = git remote | Select-String "origin"

if ($remote_exists) {
    Write-Host "⚠️  Remote 'origin' já existe. Removendo..." -ForegroundColor Yellow
    git remote remove origin
}

# Adicionar remote
Write-Host "1️⃣  Adicionando remote origin..." -ForegroundColor Cyan
git remote add origin $repo_url

# Renomear branch
Write-Host "2️⃣  Renomeando branch para 'main'..." -ForegroundColor Cyan
git branch -M main

# Mostrar status
Write-Host ""
Write-Host "3️⃣  Status atual:" -ForegroundColor Cyan
git remote -v
Write-Host ""

# Preparar para push
Write-Host "4️⃣  Preparando para fazer push..." -ForegroundColor Cyan
Write-Host ""

# Informações sobre autenticação
Write-Host "⚠️  IMPORTANTE: Você será pedido para autenticar!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Opções de autenticação:" -ForegroundColor Cyan
Write-Host "  1. Token PAT (Personal Access Token)" -ForegroundColor Green
Write-Host "     - Gere em: https://github.com/settings/tokens" -ForegroundColor Gray
Write-Host "     - Cole quando solicitado para 'password'" -ForegroundColor Gray
Write-Host ""
Write-Host "  2. GitHub CLI (Recomendado)" -ForegroundColor Green
Write-Host "     - Execute primeiro: gh auth login" -ForegroundColor Gray
Write-Host ""

# Fazer push
Write-Host "5️⃣  Fazendo push para GitHub..." -ForegroundColor Cyan
Write-Host ""

try {
    git push -u origin main
    Write-Host ""
    Write-Host "✅ SUCESSO! Integração completa!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Seu repositório está em:" -ForegroundColor Green
    Write-Host "   https://github.com/$github_user/PDV" -ForegroundColor Green
}
catch {
    Write-Host ""
    Write-Host "❌ Erro ao fazer push. Verifique:" -ForegroundColor Red
    Write-Host "   - Nome de usuário está correto"
    Write-Host "   - Você fez login no GitHub (gh auth login)"
    Write-Host "   - Seu token PAT é válido"
}

Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "  Integração Finalizada" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
