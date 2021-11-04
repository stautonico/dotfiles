#!/bin/sh
function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

# Autostart programs
#run picom --experimental-backend &
run picom &
run nitrogen --restore &
run xfce4-clipman
run /usr/bin/discord-canary

# Set proper video mode
xrandr --output HDMI-0 --mode 2560x1440 --rate 144.00 --right-of DP-4
xrandr --output DP-4 --primary --mode 2560x1440 --rate 144.00 --left-of HDMI-0

# Enable numlock on start
numlockx on

# Set mouse sensitiviy
xinput --set-prop 9 'libinput Accel Speed' -0.5

# Update Kensington Expert settings
/home/steve/Documents/Scripts/Kensington_Expert_Setup.sh
