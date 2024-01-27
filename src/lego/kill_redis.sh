#!/bin/bash
# you do not know the directory. where is the PWD of a process?
# there will be some return values.
# kill all not running locally, and launch the auto saving daemon if not launched.
# what's next? onward to redis relocation.
# we need to break here. there are no findings here.
hello_world () {
	ps -A | grep -E " redis-server\$" | python3 pgrep.py | python3 ppwdx.py | python3 proc_grep.py | python3 exam_and_run.py
}

goodbye_world () {
	ps aux | grep " python3 " | grep -E " autosave_redis.py [0-9]+\$" | python3 pgrep.py | python3 ppwdx.py | python3 proc_grep.py | python3 exam_and_run_autosave.py 
}
hello_world
# if not, just return the pid back.
# this time taking a single argument.
pwy=$(ps -A | grep -E " redis-server\$" | python3 pgrep.py | xargs)
./check_daemon_multiargs.sh $pwy
pwx=$?
#echo "main server $pwx"
if [ $pwx -eq 0 ]
then
	echo "killing non-daemon $pwy"
	kill $pwy
	hello_world
fi

# what if having multiple things?
goodbye_world
# argument is wrong.
pwy=$(ps aux | grep " python3 " | grep -E " autosave_redis.py [0-9]+\$" | python3 pgrep.py | xargs)
./check_daemon_multiargs.sh $pwy
pwx=$?
#echo "watchdog $pwx"
if [ $pwx -eq 0 ]
then
	echo "killing non-daemon $pwy"
	kill $pwy
	goodbye_world	
fi

# you can run this script after it is running.
# after killing this, we must check the special crafted thing is running.
# you are getting the trimmed thing.
# pwdx.
# finding not within the directory.
# can't you use a better tool?
