#!/usr/bin/env bash

# Kill all existing polybar instances (prevent multiple instnaces)
killall -q polybar

# Wait untill all polybar instances have been shutdown
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

polybar --config=$HOME/.config/polybar/config left &
polybar --config=$HOME/.config/polybar/config right &

# polybar --config=/home/steve/.config/polybar/config_right right &
# polybar --config=/home/steve/.config/polybar/config_left left &


echo "Launched polybar..."
