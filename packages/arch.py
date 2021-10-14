import os

packages = ['anki',
'base-devel',
'bat',
'copyq',
'fzf',
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
'tlp',
'ttf-fira-code',
'ttf-jetbrains-mono',
'ttf-nerd-font-symbols',
'vlc', 
'xclip', 
'xsel',
'zsh'
]

for item in packages:
    command = 'sudo pacman -S '+item+' --needed --noconfirm'
    os.system(command)
