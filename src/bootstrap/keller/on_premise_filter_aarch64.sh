#!/data/data/com.termux/files/usr/bin/bash
get_checked(){
	# parameters are not named.
	echo $1
}
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
res0=$(echo $(./check_mount_aarch64.sh | grep -i cpu | awk '{print $2}'))
IFS=' '
read -ra ADDR <<<"$res0"
ARRAY=()
for i in "${ADDR[@]}";
do
	target_string="cpu.cfs_quota_us"
	echo_string=$( get_checked $(sudo ls $i -1 | grep -i $target_string) )
	if [ "$target_string" == "$echo_string" ]; then
		# use this directory. append to candidate list.
		ARRAY+=$i
	else
		:
		# this is when things going philosophical.
		# the null command.
	fi
#	echo "delimiter"
# check if it has the thing.
# then make the subfolder. you might want to do it. any python bindings on cgroups?
# worst day of my life.
# might be used by cgroup2.
done

candidates=${#ARRAY[@]}
#candidates=0
if [ $candidates -gt 0 ]; then
	tardir=${ARRAY[0]}
	target_string="blitx"
	echo_string=$( get_checked $(sudo ls $tardir -1 | grep -i $target_string) )
	if [ "$target_string" == "$echo_string" ]; then
		:
	else
		sudo mkdir $tardir/blitx
		# this is when things going philosophical.
		# the null command.
	fi
	sudo bash -c "echo 20000 > $tardir/blitx/cpu.cfs_quota_us"
	sudo bash -c "echo 50000 > $tardir/blitx/cpu.cfs_period_us"
	# do the stuff then.
	# return the directory, for future use.
	echo $tardir/blitx/cgroup.procs
	# check if there's blitx directory.
#	echo "No candy"
else
	# check kernel support first.
	if get_kernel; then
		default_cpu=/sys/fs/cgroups/cpu
		sudo mkdir -p $default_cpu/blitx 
		sudo mount -t cgroup -o cpu none $default_cpu
		# if this fails, might be used by cgroup-v2, and we need to redefine the function.
		# really? not know.
		sudo bash -c "echo 20000 > $default_cpu/blitx/cpu.cfs_quota_us"
		sudo bash -c "echo 50000 > $default_cpu/blitx/cpu.cfs_period_us"
		# do the stuff then.
		# return the directory, for future use.
		echo $default_cpu/blitx/cgroup.procs
	else
		echo none
	fi
#	echo "yes man"
# might have to handle the launcher yourself.
fi
#for i in "${ARRAY[@]}"
#do
#	echo $i
#done
