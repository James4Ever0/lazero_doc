#!/data/data/com.termux/files/usr/bin/bash
# cd $(dirname $0)
## unset LD_PRELOAD in case termux-exec is installed
./aloadroot.sh
./loadram.sh
unset LD_PRELOAD
command="sudo proot"
command+=" --link2symlink"
command+=" -0"
command+=" -r alpine-ro"
command+=" -b /dev"
command+=" -b /proc"
command+=" -b ramdisk:/ramdisk"
## uncomment the following line to have access to the home directory of termux
#command+=" -b /data/data/com.termux/files/home:/root"
## uncomment the following line to mount /sdcard directly to /
#command+=" -b /sdcard"
command+=" -w /root"
command+=" /bin/busybox env -i"
command+=" HOME=/root"
command+=" PATH=/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin"
command+=" TERM=$TERM"
command+=" LANG=C.UTF-8"
command+=" /bin/busybox sh"
com="$@"
if [ -z "$1" ];then
    exec $command
else
    $command -c "$com"
fi
