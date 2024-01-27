#!/bin/bash
#kern=$(cat SEED)
#echo $kern
# that is not. i need to read line by line.
#read -d ADDR <<< "$kern"
IFS=$'\n' read -d '' -r -a lines < SEED
for i in "${lines[@]}";
do
	echo $i
done
