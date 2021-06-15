$Packages = 'base-devel',
'bat',
'copyq',
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
'the_silver_searcher',
'telegram-desktop',
'tlp',
'vlc', 
'xclip', 
'xsel', 
'zsh'

ForEach ($PackageName in $Packages){
    pacman -S $PackageName --needed --noconfirm
}
