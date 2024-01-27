#!/usr/bin/env python3
import os
import sys
from select import select
from subprocess import Popen, PIPE
# it works somehow.
with Popen(['stdbuf', '-oL', '-e0', 'curl', 'cn.bing.com'],
           stdout=PIPE, stderr=PIPE) as p:
    readable = {
        p.stdout.fileno(): sys.stdout.buffer, # log separately
        p.stderr.fileno(): sys.stdout.buffer,
    }
    while readable:
        for fd in select(readable, [], [])[0]:
            data = os.read(fd, 1024) # read available
            if not data: # EOF
                del readable[fd]
            else: 
                readable[fd].write(data)
                readable[fd].flush()
