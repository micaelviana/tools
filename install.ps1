Write-Host "=========INSTALLERS========="
Write-Host "1 - Manjaro Packages"
Write-Host "2 - AUR Packages (do not run in Root mode)"
Write-Host "3 - Ubuntu Packages"
Write-Host "4 - WSL Packages"

$op = Read-Host -Prompt "Input your option"

# Write-Host "Your Option: $op"

if($op -eq  1){
    Write-Host "Selected Option: Manjaro"
    pwsh packages/manjaro.ps1
}
elseif($op -eq  2) {
    Write-Host "Selected Option: AUR"
    pwsh packages/aur.ps1
}
elseif($op -eq  3) {
    Write-Host "Selected Option: Ubuntu"
    pwsh packages/ubuntu.ps1
}
elseif($op -eq  4) {
    Write-Host "Selected Option: WSL-Ubuntu"
    pwsh packages/wsl-ubuntu.ps1
}
else{
    Write-Host "Exit"
}