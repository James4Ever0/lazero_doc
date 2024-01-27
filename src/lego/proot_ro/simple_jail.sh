#!/bin/bash
./loadroot.sh
./loadram.sh
#cp libjudger.so.amd64 ramdisk/libjudger.so
#rm ramdisk/tmux
touch ramdisk/tmux
# simple hack.
proot -r root -b ramdisk:/ramdisk -b ramdisk/tmux:$(which tmux) -w /ramdisk
#proot -r root -b ramdisk:/ramdisk -w /ramdisk /ramdisk/libjudger.so --seccomp_rule_name="randomfuck" --exe_path=/bin/sh
