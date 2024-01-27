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
#mkdir -p ramdisk/ramdisk
# not able to execute script!
# do not use double seccomp rules!
#firejail --noprofile --read-only=/ --private=ramdisk/ ./jbash.sh
#firejail --noprofile --read-only=/ --read-only=ramdisk/libjudger.so --read-only=ramdisk/jpython.sh --read-only=ramdisk/jbash.sh --read-write=ramdisk/ramdisk --private=ramdisk/ ./jbash.sh
#firejail --noprofile --read-only=/ --private=ramdisk/ 
E
#firejail --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,shutdown ./jbash.sh
firejail --apparmor --blacklist=/sbin --blacklist=/usr/sbin --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,shutdown --rlimit-as=50000000 --rlimit-fsize=5000 --rlimit-cpu=1 --rlimit-fsize=100 --rlimit-nproc=10 --rlimit-sigpending=3
#./jbash.sh
#firejail  --apparmor --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,shutdown 
# we'll block all sbin.
# and this is useless.
#firejail  --read-only=/ --private=ramdisk/ --seccomp=!shutdown,!restart_syscall
#firejail --noprofile --read-only=/ --private=ramdisk/ --seccomp.drop=@reboot,@mount,@chown
#--seccomp.print
# this is shit.
