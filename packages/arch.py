import os

packages = ['anki',
'base-devel',
'bat',
'copyq',
'git',
'go',
'lsd',
'neofetch',
'neovim',
'nodejs',
'noto-fonts-emoji',
'npm',
'python-neovim',
'python-pip',
'qbittorrent',
'the_silver_searcher',
'telegram-desktop',
'tilix',
'tlp',
'vlc', 
'xclip', 
'xsel', 
'zsh'
]

for item in packages:
    command = 'sudo pacman -S '+item+' --needed --noconfirm'
    os.system(command)
