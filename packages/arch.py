import os

packages = ['base-devel',
'bat',
'copyq',
'fzf',
'go',
'lsd',
'neofetch',
'neovim',
'noto-fonts-emoji',
'python-neovim',
'python-pip',
'qbittorrent',
'the_silver_searcher',
'telegram-desktop',
'ttf-fira-code',
'ttf-jetbrains-mono',
'ttf-nerd-fonts-symbols',
'vlc', 
'xclip', 
'xsel',
'zoxide',
'zsh'
]

for item in packages:
    command = 'sudo pacman -S '+item+' --needed --noconfirm'
    os.system(command)
