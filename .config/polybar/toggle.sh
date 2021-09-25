if pgrep -x "polybar" > /dev/null
    then
        killall -q polybar
    else
        /home/steve/.config/polybar/launch.sh
fi
