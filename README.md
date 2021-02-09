# Dotfiles

## Ubuntu
    
* ### PopOs Repository
    [PopOs APT Repositories](https://apt.pop-os.org/)
 
* ### Extras
    [Ulauncher](https://ulauncher.io/)
    
    [LSD](https://github.com/Peltoche/lsd)


* ### Nodejs
    ```sh
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

## Manjaro

* ### AUR Helper
    ```sh
    sudo pacman -S --needed base-devel git go
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -si
    ```
    
## Windows

* ### Neovim Clipboard
    ```sh
    curl -sLo/tmp/win32yank.zip https://github.com/equalsraf/win32yank/releases/download/v0.0.4/win32yank-x64.zip
    unzip -p /tmp/win32yank.zip win32yank.exe > /tmp/win32yank.exe
    chmod +x /tmp/win32yank.exe
    mv /tmp/win32yank.exe /bin
    ```

* ### Explorer Context Menu Integration for Windows Terminal
    [Directions](https://github.com/BroJenuel/Explorer-Context-Menu-Integration-for-windows-terminal/)

## Shell
[OH MY ZSH](https://ohmyz.sh/)

[ZSHRC](https://gist.github.com/micaelviana)

## Downloads
[Sweet Theme](https://www.gnome-look.org/p/1253385/)

[Kvantum](https://store.kde.org/p/1294013/)

[Cursor](https://www.gnome-look.org/p/1393084/)

[Icon Pack](https://www.gnome-look.org/s/Gnome/p/1279924)

[Fonts](https://github.com/ryanoasis/nerd-fonts/releases/)
