#!/bin/bash

if [[ "$1" ]]; then
	files_count=$1
else
	files_count=1
fi

for (( i=1; i <= $files_count; i++ ))
do
date_marker=`date +"%Y%m%d-%H%M%S"`
echo text_${date_marker} > test_${date_marker}_sh_.txt
sleep 1s
done 

echo done