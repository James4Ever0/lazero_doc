#!/data/data/com.termux/files/usr/bin/bash
file_target=$( ./on_premise_filter_aarch64.sh )
cd bin/linux/aarch64
#./libjudger.so --exe_path=$(which bash) --seccomp_rule_name="randomfuck" --max_cpu_time=500 --max_real_time=5000 --max_memory=14213120 --max_stack=500000 --max_process_number=2 --args="--rcfile" --args="../../../bashrc"
# does that work without intervention?
while true
do
	sudo bash -c "chmod 777 $file_target"
	sudo bash -c "echo $$ > $file_target"
	if [ $? -eq 0 ]; then
		break
	fi
	cd ../../../
	sudo bash -c "./launcher_aarch64_linux.sh"
	exit 0
done

sudo ./libjudger.so --exe_path=$(which bash) --seccomp_rule_name="random"  --max_cpu_time=500 --max_real_time=10000 --max_memory=14213120 --max_stack=500000 --max_process_number=2  --input_path=/proc/self/fd/0 --output_path=/proc/self/fd/1 --error_path=/proc/self/fd/2 --uid=0 --gid=0 --args="--rcfile" --args="../../../bashrc"
