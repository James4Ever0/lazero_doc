#!/bin/bash
# checking avaliable localhost ports?
# let's just create some protocol here.
# getting avaliable list of things.
./check_ports.sh
# do it one by one.
# so this is not ideal.
# how to get the desired port? get the info back with me.
# some info from unknown.
cat ports.log | xargs -I % bash -c "echo -e '\ninfo from %\n' && curl --max-time 1 http://localhost:%/uuid" &> server_info.log
cat server_info.log | python3 server_discover.py | python3 random_chooser.py 
# you are gonna compare.
# so getting something.
# choose a random port.
