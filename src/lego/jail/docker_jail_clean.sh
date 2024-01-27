#!/bin/bash
# but we're still far from reach, cannot make it running on android phone!
#firejail --apparmor --read-only=/ --private=ramdisk/ --rlimit-as=50000000 --rlimit-fsize=5000 --rlimit-cpu=1 --rlimit-fsize=100 --rlimit-nproc=10 --rlimit-sigpending=3
firejail --overlay-clean
# no that won't solve the problem.
# all files are kept after invocation.
