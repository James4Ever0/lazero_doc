#!/bin/bash
python3 webinit.py "ls" "ls" "echo something"  "ls" "ls" "echo something" "ls" "ls" "echo something"  & sleep 10 && kill $!
