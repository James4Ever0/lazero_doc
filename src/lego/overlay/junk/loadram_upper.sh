#!/bin/bash
./unloadram_upper.sh
sudo mkdir fs/upper
sudo chmod 777 fs/upper
sudo mount -t tmpfs -o size=10m myramdisk_upper fs/upper
