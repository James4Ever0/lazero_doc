#!/bin/bash
./libjudger.so --seccomp_rule_name="randomfuck" --exe_path=/sbin/shutdown --args="0"
#./libjudger.so --exe_path=/sbin/shutdown --args="0"
# this cannot be run.
