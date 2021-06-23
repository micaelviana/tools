#!/usr/bin/env bash

wget https://raw.githubusercontent.com/dracula/gedit/master/dracula.xml -P /tmp
mkdir .local/share/gedit/      
mkdir .local/share/gedit/styles
mv /tmp/dracula.xml $HOME/.local/share/gedit/styles/
