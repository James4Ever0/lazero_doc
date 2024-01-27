#!/bin/bash
# who cares? it is all about the kernel. all relatively simple.
# not this?
pstree $1 -p -s -T | python3 check_daemon.py $1
# we do not need to understand the whole tree.
