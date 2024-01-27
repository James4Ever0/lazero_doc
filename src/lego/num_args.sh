#!/bin/bash
echo "argument length $#"
num=$#
org=$num
for var in "$@"
do
	echo "argument $var"
	num=$(($num - 1))
done
echo "final counter $num"
echo "original counter $org"
exit 2
