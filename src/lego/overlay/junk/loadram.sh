#!/bin/bash
./unloadram.sh
#sudo mkdir ramdisk
sudo mkdir fs/workdir
sudo chmod 777 fs/workdir
sudo mount -t tmpfs -o size=10m myramdisk_workdir fs/workdir
