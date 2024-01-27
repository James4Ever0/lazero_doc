#!/bin/bash
xdotool search --any --pid 3193
echo ______SPILTER______
xdotool search --onlyvisible --pid 3193
# useful even minimized
echo ______SPILTER______
xprop -id 46137345
# check for class name? not stable.
