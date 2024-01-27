#!/bin/bash
# use global variable.
# heck.
retval=""
# it is not going to work. captcha here. maybe use internal browser as a solution. create a server inside? manual server, getting quest from the localhost and post it back.
function arbitrary(){
	CLO=$(echo "$1" | python3 curl_baidu.py)
#	echo $CLO
	retval=$(links -source "$CLO")
	#retval=
	#return "hello world"
	# only numeric.
}
IFS=$'\n' read -d '' -r -a lines < SEED
for i in "${lines[@]}";
do
	echo $i
	arbitrary "$i"
#	echo $?
	echo $retval | curl --header 'Content-Type: text/html; charset=UTF-8' --request POST --data-binary @- --no-buffer http://localhost:7777/keller
# and that's your fucking dream.
done
# store it into variables.
