#!/usr/bin/env python3
import errno
import os
import pty
import sys
from select import select
from subprocess import Popen

masters, slaves = zip(pty.openpty(), pty.openpty())
with Popen(["cat"],
           stdout=slaves[0], stderr=slaves[1]):
    for fd in slaves:
        os.close(fd) # no input
    readable = {
        masters[0]: sys.stdout.buffer, # log separately
        masters[1]: sys.stderr.buffer,
    }
    while readable:
        for fd in select(readable, [], [])[0]:
            try:
                data = os.read(fd, 1024) # read available
            except OSError as e:
                if e.errno != errno.EIO:
                    raise #XXX cleanup
                del readable[fd] # EIO means EOF on some systems
            else:
                if not data: # EOF
                    del readable[fd]
                else:
                    readable[fd].write(data)
                    readable[fd].flush()
for fd in masters:
    os.close(fd)
