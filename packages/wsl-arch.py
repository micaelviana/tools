import os

packages = ['archlinux-keyring',
'btop', 
'base-devel',
'bat',
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

for item in packages:
    command = 'sudo pacman -S '+item+' --needed'
    os.system(command)
