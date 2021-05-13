$Packages = 'base-devel',
'bat'
'git',
'go',
'lsd',
'neofetch',
'neovim',
'nodejs',
'npm',
'python-neovim',
'python-pip',
'qbittorrent',
'qt5ct',
'the_silver_searcher',
'telegram-desktop',
'tilix',
'tlp',
'uget',
'vlc'

ForEach ($PackageName in $Packages){
    pacman -S $PackageName --needed --noconfirm
}
