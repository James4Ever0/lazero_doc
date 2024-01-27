#!/bin/bash
./unloadroot.sh
sudo mkdir fs/lower
sudo chmod 777 fs/lower
sudo mount --bind -r / fs/lower/
