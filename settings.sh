#!/usr/bin/env bash

#grant permission
chmod +x *.sh

#run scripts
#Setup Git (Website: http://www.erikdubois.be):
bash scripts/setup-git.sh
#Tilix Theme
bash scripts/tilix.sh
#Gedit Theme
bash scripts/gedit.sh
#ZSH 
bash scripts/zsh.sh
#Clone Vi config
bash scripts/vi.sh
