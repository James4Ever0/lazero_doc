#!/bin/bash
# check if the thing is running properly.
redis-cli bgsave
# check the time.
sleep 1
#echo sleep done
python3 redis_checker.py 
ecp=$?
echo $ecp
# use this value somehow. kill redis server running elsewhere.
# check if it is here.
# if getting that value, then we'll return.
