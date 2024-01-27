#!/bin/bash
./aunloadroot.sh
mkdir alpine-ro
chmod 777 alpine-ro
# there's autodetect.
#better use bindfs as standard.
sudo $PWD/bindfs/src/bindfs -r alpine alpine-ro
