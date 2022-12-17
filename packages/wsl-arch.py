import os

packages = ['archlinux-keyring',
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
'tmux',
'xclip', 
'xsel',
'zoxide',
'zsh'
]

for item in packages:
    command = 'sudo pacman -S '+item+' --needed'
    os.system(command)
