#!/usr/bin/env bash

#Setup Git (Website: http://www.erikdubois.be):
chmod +x scripts/setup-git.sh
bash scripts/setup-git.sh

#Setup Ranger
chmod +x scripts/ranger.sh
bash scripts/ranger.sh

#Tilix Theme
chmod +x scripts/tilix.sh
bash scripts/tilix.sh

#ZSH PLUGIN MANAGER
chmod +x scripts/zsh-plugin-manager.sh
bash scripts/zsh-plugin-manager.sh

#Clone Vi config
chmod +x scripts/vi.sh
bash scripts/vi.sh
