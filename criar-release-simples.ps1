# Script simples para criar release via Git Tags (sem precisa de API token)

cd "c:\Users\rusla\OneDrive\Documentos\PDV"

# A tag v1.0.0 já existe
# Agora vamos criar um arquivo ZIP com os arquivos compilados

Write-Host "📦 Criando arquivo para release..." -ForegroundColor Cyan

# Criar pasta temporária
$tempDir = "dist_release"
if (Test-Path $tempDir) { Remove-Item -Recurse -Force $tempDir }
New-Item -ItemType Directory -Path $tempDir | Out-Null

# Copiar arquivos principais
Copy-Item "src" -Destination "$tempDir/src" -Recurse
Copy-Item "README.md" -Destination "$tempDir/README.md"
Copy-Item "requirements.txt" -Destination "$tempDir/requirements.txt"
Copy-Item "EXECUTAR.md" -Destination "$tempDir/EXECUTAR.md"

# Criar ZIP
Compress-Archive -Path $tempDir -DestinationPath "PDV-v1.0.0.zip" -Force

Write-Host "✅ Arquivo criado: PDV-v1.0.0.zip" -ForegroundColor Green
Write-Host "📤 Agora faça upload no GitHub:" -ForegroundColor Yellow
Write-Host "   https://github.com/barretgomes/PDV/releases/tag/v1.0.0" -ForegroundColor Cyan

# Abrir no navegador
Start-Process "https://github.com/barretgomes/PDV/releases/tag/v1.0.0"

# Limpar
Remove-Item -Recurse -Force $tempDir
