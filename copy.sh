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
    # We really don't want the user prefs here (passwords are stored and stuff)
    rm -rfv ./desktop/.config/ulauncher/ext_preferences/
    cp -rv ~/.doom.d/ ./desktop/

}

case $(cat /etc/hostname) in
  (anarchy) backup_desktop;;
  (*)   echo "Unsupported device!";;
esac

