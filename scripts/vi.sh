#!/usr/bin/env bash

#clone repo
git clone https://github.com/micaelviana/nvim.git $HOME/.config/nvim

#vim-plug
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

#Install plugins
nvim +PlugInstall +qall
