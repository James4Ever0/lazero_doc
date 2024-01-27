#!/data/data/com.termux/files/usr/bin/bash
sudo mount | grep -i cgroup | awk '{print $1" " $3" " $6}'
