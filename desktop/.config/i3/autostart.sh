#!/bin/sh
function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

# Autostart programs
eval $(gnome-keyring-daemon --start)
export SSH_AUTH_SOCK
#run picom --experimental-backend &
run picom -b -c -C -G &
run nitrogen --restore &
# run xfce4-clipman
# run /usr/bin/discord --no-sandbox
run /usr/bin/discord-canary --no-sandbox

# Set proper video mode
xrandr --output HDMI-0 --mode 2560x1440 --rate 100.00 --right-of DP-2
xrandr --output DP-2 --primary --mode 2560x1440 --rate 120.00 --left-of HDMI-0

run dunst

# Enable numlock on start
numlockx on

# Set the button repeat rate
xset r rate 300 50

# Set mouse sensitiviy
xinput set-prop 11 'libinput Accel Speed' -0.5
xinput set-prop 9 'libinput Accel Speed' -0.5

# Update Kensington Expert settings
/home/steve/Documents/Scripts/Kensington_Expert_Setup.sh

# Set trackball sensitiviy
xinput set-prop 17 'libinput Accel Speed' -0.75
xinput set-prop 20 'libinput Accel Speed' -0.75
xinput set-prop 21 'libinput Accel Speed' -0.75

systemctl --user start ulauncher

/home/steve/.config/polybar/launch.sh

emacs --daemon
