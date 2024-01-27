#!/bin/bash
while true
do
	sudo yarn global add canvas 
	if [ $? -eq 0 ]; then
                break
	fi
done
