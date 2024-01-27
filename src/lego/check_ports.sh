#!/bin/bash
nmap -p- localhost | grep open | grep -Eo "^[0-9]+" > ports.log
#cat ports.log
# whatever. it will work.
# fuck. it is all meaningless.
