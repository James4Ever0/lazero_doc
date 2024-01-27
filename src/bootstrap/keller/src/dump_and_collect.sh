#!/bin/bash
# dump firefox. don't know how to do this in Windows. Maybe use Cheat Engine?
# nowhere to hide this time.
# and still don't know about android. why the fuck my /dev/shm won't work?
# you can pipe the output to python script. don't worry. just print it out.
# do a fifo stuff. maybe sandbox can read it.
ffx=$(ps -A | grep firefox | awk '{print $1}')
#gdb -p $ffx dump memory /dev/shm/dump
gcore -a -o /dev/shm/dump $ffx
