#!/bin/bash

if [[ "$1" && "$2" ]]; then
	file_name=`date +"%Y%m%d-%H%M%S"`_sh_${2}MB_.$1
	touch $file_name
	size_kb=$(($2 * 1048576))
	truncate --size $size_kb $file_name
	echo done
else
	echo Enter 'Extention' and 'Size'
fi