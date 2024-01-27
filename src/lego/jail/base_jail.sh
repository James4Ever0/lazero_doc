#!/bin/bash
# that one is not right, which will quit and leave everything unconfigured.
# you know that i just want to trap that thing into the folder.
./unloadram.sh
sudo mkdir ramdisk
sudo chmod 777 ramdisk
sudo mount -t tmpfs -o size=10m myramdisk ramdisk
# what the fuck is going on?
# wtf? try to block everything.
# how about copy things into that thing?
cp republica/* ramdisk/
chmod 777 ramdisk/*
#mkdir -p ramdisk/ramdisk
# not able to execute script!
# do not use double seccomp rules!
firejail --noprofile --read-only=/ --private=ramdisk/ ./jbash.sh
#firejail --noprofile --read-only=/ --read-only=ramdisk/libjudger.so --read-only=ramdisk/jpython.sh --read-only=ramdisk/jbash.sh --read-write=ramdisk/ramdisk --private=ramdisk/ ./jbash.sh
#firejail --noprofile --read-only=/ --private=ramdisk/ 
#firejail --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,shutdown ./jbash.sh
#firejail  --apparmor --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,shutdown
#./jbash.sh
#firejail  --apparmor --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,shutdown 
# we'll block all sbin.
# and this is useless.
#firejail  --read-only=/ --private=ramdisk/ --seccomp=!shutdown,!restart_syscall
#firejail --noprofile --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,@mount,@chown
#--seccomp.print
# this is shit.
