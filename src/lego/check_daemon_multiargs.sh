#!/bin/bash
# who cares? it is all about the kernel. all relatively simple.
# not this?
# check the length. the argument length.
edy=$#
edv=$edy
for var in "$@"
do
	echo "examing process $var"
	pstree $var -p -s -T | python3 check_daemon.py $var
	edx=$?
	if [ $edx -eq 0 ]
	then
		edy=$(($edy - 1))
		echo "killing non-daemon $var"
		kill $var
	fi
done

if [ $edy -eq $edv ]
then
	exit 1
fi
exit 0
# we do not need to understand the whole tree.
