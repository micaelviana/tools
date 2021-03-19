#!/usr/bin/env bash

# Plugin Manager for ZSH
git clone https://github.com/tarjoilija/zgen.git "${HOME}/.zgen"

#Repo from Spacehimp prompt
git clone https://github.com/denysdovhan/spaceship-prompt.git "$ZSH_CUSTOM/themes/spaceship-prompt" --depth=1

#Symlink spaceship.zsh-theme to your oh-my-zsh custom themes directory:
ln -s "$ZSH_CUSTOM/themes/spaceship-prompt/spaceship.zsh-theme" "$ZSH_CUSTOM/themes/spaceship.zsh-theme" 
