#!/bin/bash
./unloadroot.sh
sudo mkdir root
sudo chmod 777 root
sudo mount --bind -r / root/
