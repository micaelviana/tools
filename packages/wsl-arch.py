import os

packages = ['base-devel',
'bat',
'fd',
'fzf',
'lsd',
'neofetch',
'neovim',
'python-neovim',
'python-pip',
'ripgrep',
'xclip', 
'xsel',
'zoxide',
'zsh'
]

for item in packages:
    command = 'sudo pacman -S '+item+' --needed --noconfirm'
    os.system(command)
