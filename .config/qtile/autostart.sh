#!/bin/sh
function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

run picom --experimental-backend &
run nitrogen --restore &
run xfce4-clipman

# Set proper video mode
xrandr --output HDMI-0 --mode 2560x1440 --rate 144.00 --right-of DP-2
xrandr --output DP-2 --primary --mode 2560x1440 --rate 144.00 --left-of HDMI-0

# Enable numlock on start
numlockx on
