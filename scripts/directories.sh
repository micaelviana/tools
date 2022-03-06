#!/usr/bin/env bash

#create programming folder
[ ! -d $HOME/programming ] && mkdir -p $HOME/programming/{poc,projects,repos}

#create folder to download binaries
[ ! -d $HOME/.local/bin ] && mkdir -p $HOME/.local/bin

#create config folder
[ ! -d $HOME/.config ] && mkdir -p $HOME/.config

echo "programming folder is ready"
echo "local/bin folder is ready"
