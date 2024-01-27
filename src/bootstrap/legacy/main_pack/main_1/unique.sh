#!/bin/bash
# find all point of interest.
# len 1, len 2, convolution.
number=$(cat /dev/shm/lazero | wc -c)
# echo $number
rounds=1
# formula -> [x:y] head -c y | tail -c y-x
# what the fuck?
# shit code.
# k=10
while [ $rounds -le 10 ]
do
y=0
f=$[$number-$rounds]
echo $f
while [ $y -le $f ]
do
sample=$(cat /dev/shm/lazero | head -c $y | tail -c $rounds)
cat /dev/shm/lazero | rg "$sample"
echo "___________spliter___________"
y=$[y+1]
done
rounds=$[rounds+1]
done
# no one will keep good grammar. if people talk shit, i don't have to.
# man i want to do this in python script. this sucks.
# read something and automatically get the collections right.
# guess this is the right place to do the thing.
# i want secondary order logic!