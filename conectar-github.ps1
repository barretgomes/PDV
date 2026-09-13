# Script Simplificado para Conectar GitHub

Write-Host ""
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "  Conectar PDV ao GitHub" -ForegroundColor Cyan
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host ""

# Pedir username
$user = Read-Host "Digite seu usuario GitHub (ex: joaosilva)"

if ([string]::IsNullOrWhiteSpace($user)) {
    Write-Host ""
    Write-Host "Erro: Usuario nao pode estar vazio!" -ForegroundColor Red
    exit 1
}

$url = "https://github.com/$user/PDV.git"

Write-Host ""
Write-Host "Configurando:" -ForegroundColor Yellow
Write-Host "  URL: $url" -ForegroundColor Gray
Write-Host ""

# PASSO 1: Adicionar remote
Write-Host "[1/3] Adicionando remote..." -ForegroundColor Cyan

# Verificar se remote ja existe
$remoteExists = git remote | Select-String "origin"

if ($remoteExists) {
    Write-Host "  Removendo remote origin existente..." -ForegroundColor Yellow
    git remote remove origin 2>$null
}

git remote add origin $url 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "  Erro ao adicionar remote!" -ForegroundColor Red
    exit 1
}
Write-Host "  OK - Remote adicionado!" -ForegroundColor Green

# PASSO 2: Renomear branch
Write-Host ""
Write-Host "[2/3] Garantindo branch 'main'..." -ForegroundColor Cyan
git branch -M main 2>&1
Write-Host "  OK - Branch 'main' configurado!" -ForegroundColor Green

# PASSO 3: Fazer push
Write-Host ""
Write-Host "[3/3] Fazendo push para GitHub..." -ForegroundColor Cyan
Write-Host "  Aguarde alguns segundos..." -ForegroundColor Gray
Write-Host ""

git push -u origin main 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "SUCESSO! Conectado ao GitHub!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Seu repositorio esta em:" -ForegroundColor Green
    Write-Host "  https://github.com/$user/PDV" -ForegroundColor Cyan
    Write-Host ""
}
else {
    Write-Host ""
    Write-Host "Erro ao fazer push!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Verifique:" -ForegroundColor Yellow
    Write-Host "  1. Voce esta logado no GitHub (execute: gh auth login)" -ForegroundColor Gray
    Write-Host "  2. O repositorio PDV existe em https://github.com/$user/PDV" -ForegroundColor Gray
    Write-Host "  3. Voce tem permissao para escrever neste repositorio" -ForegroundColor Gray
    exit 1
}

Write-Host ""
Write-Host "===================================================" -ForegroundColor Green
Write-Host "  Integracao Concluida!" -ForegroundColor Green
Write-Host "===================================================" -ForegroundColor Green
