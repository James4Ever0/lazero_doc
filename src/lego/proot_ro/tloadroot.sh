#!/bin/bash
./tunloadroot.sh
mkdir root
chmod 777 root
# there's autodetect.
#better use bindfs as standard.
sudo $PWD/bindfs/src/bindfs -r $PREFIX/ root/
