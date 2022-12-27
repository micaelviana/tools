import os

packages = ['build-essential',
'bat',
'curl',
'fd-find',
'fzf',
'gawk',
'neofetch',
'python3-pip',
'ripgrep',
'tree',
'tmux',
'xclip',
'xsel',
'wget',
'zoxide',
'zsh']

for item in packages:
    command = 'sudo nala install -y '+item
    os.system(command)
