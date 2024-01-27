#!/bin/bash
# firejail --cgroup=/sys/fs/cgroup/lazero/tasks  --apparmor --disable-mnt bash
# so what? file size and more?
firejail --rlimit-as=15000000 --rlimit-cpu=1 --rlimit-fsize=2000000  --private --blacklist=/ --read-only=/home --nonewprivs --noroot --apparmor --disable-mnt bash
# what the heck is going on? why it is able to modify shits?
