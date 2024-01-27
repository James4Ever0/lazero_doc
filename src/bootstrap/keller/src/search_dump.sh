#!/bin/bash
ro=$(pwd)
cd /dev/shm
rg -a "http" | python3 "$ro/firefox_memdump.py"
# do it more.
