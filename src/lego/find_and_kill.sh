#!/bin/bash
ps aux | grep python3 | grep webpaste.py > candidate.log
ps -A | grep python | grep -Eo "[0-9]+" > pid_matcher.log
# show the capability. the logic.
python matcher.py | xargs kill
# so nothing there, once killed.
# generate killing script.
