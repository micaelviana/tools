#!/usr/bin/env bash

#copy the default configuration
ranger --copy-config=all


#adds configuration
echo "#----------My config--------------" >> ~/.config/ranger/rc.conf


#adds relative line numbers 
echo "set line_numbers relative" >> ~/.config/ranger/rc.conf

#Image preview
echo "set preview_images true" >> ~/.config/ranger/rc.conf
echo "set preview_images_method ueberzug" >> ~/.config/ranger/rc.conf

