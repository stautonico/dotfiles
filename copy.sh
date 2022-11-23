#!/usr/bin/env bash

backup_desktop() {
    cp -rv ~/.zshrc ./desktop
    cp -rv ~/.vimrc ./desktop
    cp -rv ~/.config/nvim/ ./desktop/.config/
    cp -rv ~/.config/tilix ./desktop/.config/
    cp -rv ~/.config/katerc ./desktop/.config/
    cp -rv ~/.config/qtile ./desktop/.config/
    cp -rv ~/.config/alacritty ./desktop/.config/
    cp -rv ~/.config/rofi ./desktop/.config/
    cp -rv ~/.config/i3 ./desktop/.config/
    cp -rv ~/.config/polybar ./desktop/.config/
    cp -rv ~/.config/dunst ./desktop/.config/
    cp -rv ~/.config/flameshot ./desktop/.config/
    cp -rv ~/.config/neofetch ./desktop/.config/
    cp -rv ~/.config/picom ./desktop/.config/
    cp -rv ~/.config/ranger ./desktop/.config/
    cp -rv ~/.config/ulauncher ./desktop/.config/
    cp -rfv ~/.config/keyb ./desktop/.config/
    cp -rv ~/.gitconfig ./desktop/
    # We really don't want the user prefs here (passwords are stored and stuff)
    rm -rfv ./desktop/.config/ulauncher/ext_preferences/
    cp -rv ~/.doom.d/ ./desktop/

    # Copy the scripts over
    cp -rv ~/Documents/Scripts ./desktop/
    rm -rv ./desktop/Scripts/.ron_mod_man.json
}

backup_laptop() {
    cp -rv ~/.Xresources ./laptop/
    cp -rv ~/.config/i3 ./laptop/.config/
    cp -rv ~/.zshrc ./laptop
    cp -rv ~/.vimrc ./desktop
    cp -rv ~/.doom.d/ ./laptop/
    cp -rv ~/.config/dunst ./laptop/.config/
    cp -rv ~/.config/rofi ./laptop/.config/
    cp -rv ~/.config/picom.conf ./laptop/.config/
}

case $(cat /etc/hostname) in
  (anarchy) backup_desktop;;
  (pleasefuckingwork) backup_laptop;;
  (*)   echo "Unsupported device!";;
esac

