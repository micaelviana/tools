import os

packages = ['build-essential',
'curl',
'git',
'neovim',
'nodejs',
'python3-pip',
'silversearcher-ag',
'tmux'
'unzip',
'wget',
'zsh'
]

for item in packages:
    command = "apt install -y "+item
    os.system(command)