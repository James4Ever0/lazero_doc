#!/bin/bash
data=$(tail locate.db --lines 1)
echo $data
count=$(echo $data | wc -c)
size=$(wc -c locate.db | awk '{print $1}')
truncate -c -s $[$size-$count] locate.db