import os

packages = ['build-essential',
'caffeine',
'curl',
'neofetch',
'neovim',
'python3-pip',
'qbittorrent',
'silversearcher-ag',
'telegram-desktop',
'virtualbox',
'vlc',
'wget',
'zsh']

for item in packages:
    command = 'apt install -y '+item
    os.system(command)
