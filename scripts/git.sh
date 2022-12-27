#!/bin/bash
#
##################################################################################################################
# Written to be used on 64 bits computers
# Author 	: 	Erik Dubois
# Website 	: 	http://www.erikdubois.be
##################################################################################################################
##################################################################################################################
#
#   DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
##################################################################################################################

#setting up git
#https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config

git config --global user.name "Micael Viana"
git config --global user.email "44692237+micaelviana@users.noreply.github.com"
git config --global core.editor nvim
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=180000'
