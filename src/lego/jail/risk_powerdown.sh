#!/bin/bash
firejail --apparmor --read-only=/ --private=ramdisk/ --name=browser poweroff &
# use some sleep?
# too damn quick.
./sleep100ms
firejail --seccomp.print=browser &> poweroff.log
