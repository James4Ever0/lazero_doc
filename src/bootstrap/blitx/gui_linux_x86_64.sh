#!/bin/bash
#mkfifo blitx
# maybe we need to use some nonblocking reading.
#firejail firefox &> /dev/null & echo $!
firejail firefox &>/dev/stdout | python3 tracker_gui_linux_x86_64.py
