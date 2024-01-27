#!/bin/bash

sudo grep rw-p /proc/$1/maps \
| sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' \
| while read start stop; do \
    sudo gdb --batch --pid $1 -ex \
        "dump memory /proc/self/fd/0 0x$start 0x$stop"; \
done
