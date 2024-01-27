#!/bin/bash
limit=5
if [ $# -eq 1 ]
then
	if [ $1 -gt 0 ]
	then
		limit=$1
	fi
fi
echo "limit of process: $limit"
#limit=$(($limit + 1))
# you do not know the directory. where is the PWD of a process?
# there will be some return values.
# kill all not running locally, and launch the auto saving daemon if not launched.
# what's next? onward to redis relocation.
# we need to break here. there are no findings here.
# the naming problem. there's the thing.
goodbye_world () {
	ps aux | grep " python3 " | grep -E " webpaste.py\$" | python3 pgrep.py | python3 ppwdx.py | python3 proc_grep.py | python3 exam_and_run_webpaste.py $limit
}
# that's merging multiple arguments.
# shall kill those that running elsewhere.
goodbye_world
pwy=$(ps aux | grep python3 | grep webpaste.py | python3 pgrep.py | xargs)
#echo $pwy
# what is that thing above?
./check_daemon_multiargs.sh $pwy
# you kill all non-daemon things and return the status.
pwx=$?
# there shall be multiple elements. so what to do?
#echo "watchdog $pwx"
if [ $pwx -eq 0 ]
then
	echo "need reconfiguration"
	goodbye_world	
	exit 0
fi
echo "no need to reconfigure"
exit 0
# define the maximum server number. such as 5.
# you can run this script after it is running.
# after killing this, we must check the special crafted thing is running.
# you are getting the trimmed thing.
# pwdx.
# finding not within the directory.
# can't you use a better tool?
