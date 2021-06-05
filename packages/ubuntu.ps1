$Packages = 'bat',
'build-essential',
'caffeine',
'curl',
'neofetch',
'neovim',
'python3-pip',
'qbittorrent',
'silversearcher-ag',
'telegram-desktop',
'virtualbox',
'vlc',
'wget',
'zsh'

ForEach ($PackageName in $Packages){
    apt install $PackageName -y
}
