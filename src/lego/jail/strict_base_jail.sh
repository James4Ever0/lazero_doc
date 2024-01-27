#!/bin/bash
# that one is not right, which will quit and leave everything unconfigured.
./unloadram.sh
sudo mkdir ramdisk
sudo chmod 777 ramdisk
sudo mount -t tmpfs -o size=10m myramdisk ramdisk
# what the fuck is going on?
# wtf? try to block everything.
firejail --apparmor --read-only=/ --private=ramdisk/ --seccomp.drop=shutdown,@privileged python3
# and this is useless.
#firejail  --read-only=/ --private=ramdisk/ --seccomp=!shutdown,!restart_syscall
#firejail --noprofile --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,@mount,@chown
#--seccomp.print
# this is shit.
