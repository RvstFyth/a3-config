#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

MONITOR="HDMI-1" polybar --reload top >>/tmp/polybar1.log 2>&1 &
MONITOR="VGA-1" polybar --reload top2 >>/tmp/polybar1.log 2>&1 &

# if type "xrandr"; then
#   for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
#     MONITOR=$m polybar --reload top &
#   done
# else
#   polybar --reload top &
# fi