import os

packages = ['build-essential',
'caffeine',
'curl',
'gawk',
'gnome-tweaks',
'neofetch',
'neovim',
'python3-pip',
'qbittorrent',
'qt5ct',
'qt5-style-kvantum',
'qt5-style-kvantum-l10n',
'qt5-style-kvantum-themes',
'silversearcher-ag',
'telegram-desktop',
'tilix',
'tlp',
'virtualbox',
'vlc',
'wget',
'zsh']

for item in packages:
    command = 'sudo apt install -y '+item
    os.system(command)
