import os

packages = ['base-devel',
'bat',
'copyq',
'fd',
'fzf',
'lsd',
'neofetch',
'neovim',
'noto-fonts-emoji',
'python-neovim',
'python-pip',
'qbittorrent',
'ripgrep',
'telegram-desktop',
'tmux',
'ttf-fira-code',
'ttf-nerd-fonts-symbols',
'vlc', 
'xclip', 
'xsel',
'zoxide',
'zsh'
]

temp = ['archlinux-keyring',
'btop', 
'base-devel',
'bat',
'clang',
'fd',
'fzf',
'lsd',
'neofetch',
'neovim',
'python-neovim',
'python-pip',
'ripgrep',
'shellcheck', 
'tree',
'tmux',
'xclip', 
'xsel',
'zoxide',
'zsh',
'zip',
'tldr',
'unzip'
]

for item in temp:
    command = 'sudo pacman -S '+item+' --needed'
    os.system(command)
