#!/bin/bash

# base-devel is required for most of this stuff
sudo pacman -S base-devel --noconfirm


# Update the mirror lists
sudo pacman -S reflector rsync curl wget --noconfirm
sudo cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.bak
sudo reflector --verbose --country 'United States' -l 5 --sort rate --save /etc/pacman.d/mirrorlist

# Update the packages and do a full system upgrade
sudo pacman -Syyu --noconfirm

# Install yay AUR helper
sudo pacman -S git --noconfirm
cd /opt
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R steve:steve ./yay-git
cd yay-git
makepkg -si --noconfirm

# Install octopi aur helper
sudo pacman -S octopi --noconfirm

# Install packages through yay
yay -S --aur aur/minecraft-launcher --noconfirm --sudoloop
yay -S --aur aur/zoom --noconfirm --sudoloop
yay -S --aur aur/etcher-bin --noconfirm --sudoloop
yay -S --aur aur/jetbrains-toolbox --noconfirm --sudoloop
yay -S --aur aur/discord-canary --noconfirm --sudoloop
yay -S --aur aur/termius --noconfirm --sudoloop
yay -S --aur aur/google-chrome --noconfirm --sudoloop
yay -S --aur aur/keybase-bin --noconfirm --sudoloop
yay -S --aur aur/slack-desktop --noconfirm --sudoloop
yay -S --aur aur/teamviewer --noconfirm --sudoloop
yay -S --aur aur/makemkv --noconfirm --sudoloop
yay -S --aur aur/typora --noconfirm --sudoloop
yay -S --aur aur/ledger-live --noconfirm --sudoloop # RUN MANUALLY
yay -S --aur aur/stoplight-studio-appimage --noconfirm --sudoloop
yay -S --noconfirm zsh-theme-powerlevel10k-git --sudoloop


# Install snap and install snap packages
git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si --noconfirm

sudo systemctl enable --now snapd.socket

sudo snap install spotify


# Install packages through pacman
# Install gui/tools
sudo pacman -S libreoffice-fresh kate audacity steam krita peek signal-desktop audacity mkvtoolnix-cli mkvtoolnix-gui okular htop bpytop cura zsh nvidia firefox-developer-edition --noconfirm

# Install development tools
sudo pacman -S python-virtualenv nodejs npm sqlitebrowser jre-openjdk vim --noconfirm


# Setup NPM
sudo npm install -g nodemon typescript @angular/cli

# Manually install some other dev tools

# Stoplight Studio
# cd ~/Documents
# mkdir Apps
# cd Apps
# mkdir Dev
# cd Dev
# wget https://github.com/stoplightio/studio/releases/download/v2.3.0-stable.5602.git-d17f9c7/stoplight-studio-linux-x86_64.AppImage
# echo -e "[Desktop Entry]\nComment=\nExec=/home/steve/Documents/Apps/Dev/stoplight-studio-linux-x86_64.AppImage %U\nIcon=/home/steve/Pictures/Icons/com.stoplight.studio.png\nName=Stoplight Studio\nNoDisplay=false\nPath[$e]=\nStartupNotify=true\nTerminal=0\nTerminalOptions=\nType=Application\nX-KDE-SubstituteUID=false\nX-KDE-Username=">/usr/share/applications/stoplight-studio.desktop

# Setup /etc/fstab (and the other mount stuff)
echo -e "\n\n# STORGONJESMORF personal share" | sudo tee -a /etc/fstab
echo -e "//192.168.1.244/steven /mnt/steven cifs iocharset=utf8,credentials=/home/steve/.smbcredentials,uid=1000,vers=3.0,mfsymlinks,_netdev 0 0" | sudo tee -a /etc/fstab
echo -e "\n# STORGONJESMORF shared share" | sudo tee -a /etc/fstab
echo -e "//192.168.1.244/share /mnt/share cifs iocharset=utf8,credentials=/home/steve/.smbcredentials,uid=1000,vers=3.0,mfsymlinks,_netdev 0 0" | sudo tee -a /etc/fstab
echo -e "\n# STORGONJESMORF Media (Plex)" | sudo tee -a /etc/fstab
echo -e "//192.168.1.244/Media /mnt/Media cifs iocharset=utf8,credentials=/home/steve/.smbcredentials,uid=1000,vers=3.0,mfsymlinks,_netdev 0 0" | sudo tee -a /etc/fstab

sudo mkdir /mnt/Media
sudo mkdir /mnt/share
sudo mkdir /mnt/steven

sudo mount -a


# Install zsh + plugins
curl -L http://install.ohmyz.sh | sh
echo 'source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme' >> ~/.zshrc
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
sudo pacman -S zsh-syntax-highlighting --noconfirm
sudo git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k

echo "To install zsh plugins, edit plugins=() in ~/.zshrc to plugins=(zsh-autosuggestions zsh-syntax-highlighting k tmux kate)"
