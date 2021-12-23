#!/usr/bin/env bash

#clone repo
git clone https://github.com/micaelviana/nvim.git $HOME/.config/nvim

#Install plugins
nvim +PlugInstall +qall
