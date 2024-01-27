#!/bin/bash
firejail --apparmor --read-only=/ --private=ramdisk/ --name=browser0 reboot &
./sleep50ms
firejail --seccomp.print=browser0 &> reboot.log
