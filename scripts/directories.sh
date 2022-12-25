#!/usr/bin/env bash

#create programming folder
[ ! -d $HOME/developer ] && mkdir -p $HOME/developer/{poc,projects,repos} && echo "developer folder is ready"

#create folder to download binaries
[ ! -d $HOME/.local/bin ] && mkdir -p $HOME/.local/bin echo "local/bin folder is ready"

#create config folder
[ ! -d $HOME/.config ] && mkdir -p $HOME/.config
