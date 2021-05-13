$Packages = 'build-essential',
'curl',
'git',
'neovim',
'nodejs',
'python3-pip',
'silversearcher-ag',
'tmux'
'unzip',
'wget',
'zsh'

ForEach ($PackageName in $Packages){
    apt install $PackageName -y
}
