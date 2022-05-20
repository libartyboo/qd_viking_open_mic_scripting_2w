#!/bin/bash

extention_list=("avi bmp doc docm docx eps gif jpeg jpg key 
m4v mov mp4 mpg msg nsf odt pdf png pps ppsx ppt pptx rar 
rtf tif tiff txt wmv xls xlsb xlsm xlsx xps zip 7z")

if [[ "$1" ]]; then
	size=$1
else
	size=1
fi

for ext in $extention_list
do
size_kb=$(($size * 1048576)) 
file_name=`date +"%Y%m%d-%H%M%S"`_${ext}_${size}MB_.${ext}
touch $file_name
truncate --size $size_kb $file_name
done
echo done