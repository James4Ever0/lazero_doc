#!/bin/bash
./libjudger.so --seccomp_rule_name="randomfuck" --exe_path=$(which python)
#./libjudger.so --exe_path=/sbin/shutdown --args="0"
# this cannot be run.
