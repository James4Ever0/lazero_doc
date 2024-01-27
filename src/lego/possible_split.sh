#!/bin/bash
# feed it into a script
ps -A | grep -i python | python3 termsplit.py
