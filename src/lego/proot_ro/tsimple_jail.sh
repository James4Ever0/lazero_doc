#!/data/data/com.termux/files/usr/bin/bash
# cd $(dirname $0)
## unset LD_PRELOAD in case termux-exec is installed
./tloadroot.sh
./aloadroot.sh
./loadram.sh
chmod 777 $PREFIX/bin/*
unset LD_PRELOAD
#set LD_PRELOAD=/lib/libtermux-exec.so
#set LD_LIBRARY=/lib
command="sudo proot"
command+=" --link2symlink"
#command+=" -0"
command+=" -r alpine-ro"
command+=" -b /dev"
command+=" -b /proc"
command+=" -b root:/termux"
#command+=" -b /system/bin/env:/sbin/env"
command+=" -b ramdisk:/ramdisk"
## uncomment the following line to have access to the home directory of termux
#command+=" -b /data/data/com.termux/files/home:/root"
## uncomment the following line to mount /sdcard directly to /
#command+=" -b /sdcard"
command+=" -w /ramdisk"
command+=" /bin/busybox env -i"
command+=" HOME=/ramdisk"
command+=" PREFIX=/termux"
command+=" PATH=/termux/bin:/usr/local/sbin:/usr/local/bin:/bin:/usr/bin:/sbin:/usr/sbin"
command+=" TERM=$TERM"
command+=" LD_PRELOAD=/lib/libtermux-exec.so"
command+=" LANG=C.UTF-8"
#command+=" bash"
command+=" /bin/busybox sh"
com="$@"
if [ -z "$1" ];then
    exec $command
else
    $command -c "$com"
fi
