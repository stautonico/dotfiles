#!/usr/bin/env bash

# Kill all existing polybar instances (prevent multiple instnaces)
killall -q polybar

# Wait untill all polybar instances have been shutdown
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

polybar --config=/home/steve/.config/polybar/config steve &


echo "Launched polybar..."
