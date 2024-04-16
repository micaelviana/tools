# Tools

## Ubuntu
Backup packages

```sh
dpkg --get-selections > package_list/ubuntu.txt
```
Install packages
```sh
sudo xargs -a package_list/ubuntu.txt apt-get install
```


## Arch

Backup packages

```sh
pacman -Q > package_list/arch.txt
```
Install packages
```sh
yay -S - < package_list/arch.txt
```

 ### AUR Helper
    ```sh
    sudo pacman -S --needed git base-devel
    git clone https://aur.archlinux.org/yay-bin.git
    cd yay-bin
    makepkg -si
    ```

## Downloads
[Nerd Fonts](https://github.com/ryanoasis/nerd-fonts/releases/)

[Monaco Nerd Font](https://github.com/Karmenzind/monaco-nerd-fonts)
