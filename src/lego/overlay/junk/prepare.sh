#!/bin/bash
bash -c ./loadram_fs.sh
bash -c ./loadroot.sh
bash -c ./loadram.sh
bash -c ./loadram_upper.sh
mkdir -p fs/overlay
mount -t overlay -o rw,lowerdir=fs/lower,upperdir=fs/upper,workdir=fs/workdir overlay fs/overlay
