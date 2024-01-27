#!/bin/bash
./unloadram_fs.sh
#sudo mkdir ramdisk
sudo mkdir fs
sudo chmod 777 fs
sudo mount -t tmpfs -o size=10m myramdisk_fs fs
