import os

packages = ['base-devel',
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
]

for item in packages:
    command = 'pacman -S '+item+' --needed --noconfirm'
    os.system(command)