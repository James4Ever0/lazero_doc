#!/bin/bash
# but we're still far from reach, cannot make it running on android phone!
./unloadram.sh
sudo mkdir ramdisk
sudo chmod 777 ramdisk
sudo mount -t tmpfs -o size=10m myramdisk ramdisk
cp republica/* ramdisk/
chmod 777 ramdisk/*
firejail --noprofile --read-only=/ --private=ramdisk/ --rlimit-as=50000000 --rlimit-fsize=5000 --rlimit-cpu=1 --rlimit-fsize=100 --rlimit-nproc=10 --rlimit-sigpending=3 ./jbash.sh
#firejail --apparmor --read-only=/ --private=ramdisk/ --rlimit-as=50000000 --rlimit-fsize=5000 --rlimit-cpu=1 --rlimit-fsize=100 --rlimit-nproc=10 --rlimit-sigpending=3
# no that won't solve the problem.
# all files are kept after invocation.
