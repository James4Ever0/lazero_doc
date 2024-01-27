#!/bin/bash
get_kernel(){
	kern=$( echo $(./check_cgroups.sh | awk '{print $1}'))
	#kern=$()
	read -ra ADDR <<<"$kern"
	v=0
	for i in "${ADDR[@]}";
	do
		if [ "$i" == "cpu" ]; then
			v+=1
		else
			:
		fi
#		echo $i
	done
	echo $v
	if [ $v -ne 0 ] ; then
		return 0
	else
		return 1
	fi
}
#echo $( retval get_kernel )
if get_kernel; then
	echo "something"
else
	echo "nothing"
fi
